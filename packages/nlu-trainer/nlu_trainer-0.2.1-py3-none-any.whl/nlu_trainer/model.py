import lightning as L
from lightning.pytorch.utilities.types import EVAL_DATALOADERS, STEP_OUTPUT, TRAIN_DATALOADERS, OptimizerLRScheduler
import torch.nn as nn
from torch.utils.data import DataLoader
from nlp_data import EmbeddingDocStore
import numpy as np
import torch
from torch.optim import AdamW
from .layers import CRF, MultiDropout
from wasabi import msg
from datasets import load_from_disk, DatasetDict
from functools import lru_cache
from typing import Any, List, Literal, Optional
import pandas as pd
from nlu_inference.utils import ner_post_process
from .metrics import ChunkF1
from .utils import get_tokenizer
from .scheduler import linear_schedule_with_warmup
import json
import onnx
import os
from pathlib import Path
from typing import Union


class EntityExtractionDataModule(L.LightningDataModule):
    """实体抽取数据模块
    数据集格式: {"text":"这是一个长颈鹿","ents":[{"indices":[4,5,6],"label":"动物", "text":"长颈鹿"}]}
    """
        
    def __init__(self,
                 dataset_path: str,
                 processed_dataset_path: str,
                 embedding_name: str,
                 batch_size: int = 32,
                 max_length: int = 32,
                 pad_side: Literal['left', 'right'] = "left",
                 num_workers: int = 4,
                 lang: Literal['zho', 'eng', 'cmn'] = 'cmn',
                 process_batch_size: int = 10000,
                 **kwargs):
        super().__init__()
        self.save_hyperparameters(ignore='tokenizer')
        if Path(processed_dataset_path).exists():
            self.dataset = load_from_disk(processed_dataset_path)
            self.processed = True
        else:
            self.dataset = load_from_disk(self.hparams.dataset_path)
            self.processed = False
        self.hparams.id2bio = self.id2bio
        self.tokenizer = get_tokenizer(lang=lang, max_length=self.hparams.max_length, pad_side=self.hparams.pad_side)
        
    
    def prepare(self) -> None:
        if self.processed:
            pass
        else:
            processed_ds = self.dataset.map(self.bio_transform, batched=True, num_proc=self.hparams.num_workers, batch_size=self.hparams.process_batch_size)
            processed_dataset_dir = Path(self.hparams.processed_dataset_path)
            processed_ds.save_to_disk(processed_dataset_dir)
    
    
    def setup(self, stage: str = 'fit') -> None:
        if stage == 'fit':
            if self.processed:
                pass
            else:
                self.dataset = load_from_disk(self.hparams.processed_dataset_path)
         
    @property
    @lru_cache()
    def ent_labels(self) -> List:
        labels = sorted(pd.Series(np.concatenate(self.train_df['ents'])).apply(lambda x: x['label']).drop_duplicates().values)
        return labels
    
    @property
    def ent2id(self):
        return {l:i for i,l in enumerate(self.ent_labels)}

    @property
    def id2ent(self):
        return {i:l for l,i in self.ent2id.items()}
    
    @property
    @lru_cache()
    def bio_labels(self) -> List:
        b_labels = ['B' + '-' + l for l in self.ent_labels]
        i_labels = ['I' + '-' + l for l in self.ent_labels]
        return ['O'] + b_labels + i_labels
    
    @property
    def bio2id(self):
        return {l:i for i,l in enumerate(self.bio_labels)}
    
    @property
    def id2bio(self):
        return {i:l for l,i in self.bio2id.items()}
    
    @property
    @lru_cache()
    def train_df(self):
        return self.dataset['train'].to_pandas()
    
    @property
    @lru_cache()
    def val_df(self):
        return self.dataset['validation'].to_pandas()
    
    @property
    @lru_cache()
    def test_df(self):
        return self.dataset['test'].to_pandas()
    
    def get_batch_max_length(self, batch_text):
        return max([len(text) for text in batch_text])
    
    def bio_transform(self, examples):
        batch_text = examples['text']  
        inputs = {}
        batch_tokens = self.tokenizer(batch_text=batch_text)
        input_ids = [tokens.ids for tokens in batch_tokens]
        input_ids = torch.tensor(input_ids)
        inputs['input_ids'] = input_ids
        batch_tags = torch.zeros_like(input_ids, dtype=torch.long)
        for i, text in enumerate(batch_text):
            ents = examples['ents'][i]
            tokens = batch_tokens[i]
            for ent in ents:
                indices = ent['indices']
                start_token = tokens.char_to_token(indices[0])
                end_token = tokens.char_to_token(indices[-1])
                if start_token:
                    if not end_token:
                        end_token = len(tokens) - 1
                    batch_tags[i][start_token] = self.bio2id['B' + '-' + ent['label']]
                    if len(indices) > 1:
                        batch_tags[i][start_token+1: end_token+1] = self.bio2id['I' + '-' + ent['label']]
        inputs['tag_ids'] = batch_tags
        return inputs
    
    def train_dataloader(self) -> TRAIN_DATALOADERS:
        return DataLoader(dataset=self.dataset['train'], 
                          batch_size=self.hparams.batch_size,
                          num_workers=self.hparams.num_workers,
                          pin_memory=True,
                          collate_fn=self.collate_fn)
    
    def val_dataloader(self) -> EVAL_DATALOADERS:
        return DataLoader(dataset=self.dataset['validation'], 
                          batch_size=self.hparams.batch_size,
                          num_workers=self.hparams.num_workers,
                          pin_memory=True,
                          collate_fn=self.collate_fn)
        
    def collate_fn(self, batch):
        input_ids = torch.tensor([item['input_ids'] for item in batch], dtype=torch.long)
        tag_ids = torch.tensor([item['tag_ids'] for item in batch])
        return {'input_ids': input_ids, 'tag_ids': tag_ids}

class CRFClassifier(nn.Module):
    def __init__(self, 
                 n_tags: int, 
                 n_in: int, 
                 n_hidden: int):
        super().__init__()
        self.lstm = nn.LSTM(n_in, n_hidden, bidirectional=True, batch_first=True)
        self.dropout = MultiDropout()
        self.fc = nn.Linear(n_hidden * 2, n_tags)
        self.crf = CRF(num_tags=n_tags, batch_first=True)
        
    def forward(self, x):
        x, _ = self.lstm(x)
        x = self.dropout(x)
        x = self.fc(x)
        x = self.crf.decode(x)
        # 将输出的标签转化为one hot形式以跟之前模型兼容
        x = torch.nn.functional.one_hot(x, num_classes=self.crf.num_tags).float()
        
        return x
    
    def compute_loss(self, x, tags):
        x, _ = self.lstm(x)
        x = self.dropout(x)
        x = self.fc(x)
        loss = self.crf(emissions=x, tags=tags)
        return loss * -1
        

class CRFForEntityExtraction(L.LightningModule):
    def __init__(self, 
                 freeze_embedding: bool = False,
                 lr: float = 0.001,
                 hidden_size: int = 128,
                 **kwargs):
        super().__init__()
        self.save_hyperparameters()     
        
        self.num_labels = len(self.hparams.id2bio)
        self.embedding_docs = EmbeddingDocStore.pull(self.hparams.embedding_name)
        self.embeddings = nn.Embedding.from_pretrained(embeddings=torch.from_numpy(np.array([doc.embedding for doc in self.embedding_docs], dtype=np.float32)), freeze=self.hparams.freeze_embedding)
        self.classifier = CRFClassifier(n_tags=self.num_labels, n_in=self.embeddings.embedding_dim, n_hidden=self.hparams.hidden_size)
        self.hparams.tokenizer = get_tokenizer(lang=self.hparams.lang, max_length=self.hparams.max_length, pad_side=self.hparams.pad_side)
        
    def setup(self, stage: str):
        self.metric = ChunkF1()  
        
    def forward(self, input_ids):
        x = self.embeddings(input_ids)
        pred_ids = self.classifier(x)
        return pred_ids
    
    def compute_loss(self, input_ids, tags):
        x = self.embeddings(input_ids)
        loss = self.classifier.compute_loss(x=x, tags=tags)
        return loss
        
    def training_step(self, inputs) -> STEP_OUTPUT:
        loss = self.compute_loss(input_ids=inputs['input_ids'], tags=inputs['tag_ids'])
        self.log("train/loss", value=loss, prog_bar=True, on_step=True, on_epoch=False)
        return loss
    
    def validation_step(self, inputs) -> STEP_OUTPUT:
        pred_ids = self(input_ids=inputs['input_ids']).argmax(dim=-1)
        pred_labels = []
        for ids in pred_ids:
            pred_labels.append([self.hparams.id2bio[id] for id in ids.tolist()])
        true_label_ids = inputs['tag_ids']
        true_labels = []
        for i in range(len(true_label_ids)):
            indices = torch.where(true_label_ids[i]>=0)
            ids = true_label_ids[i][indices].tolist()
            true_labels.append([self.hparams.id2bio[id] for id in ids])
        self.metric(pred_labels, true_labels)
        self.log("val/f1", self.metric, on_step=False, on_epoch=True, prog_bar=True)
        
        
    def configure_optimizers(self) -> OptimizerLRScheduler:
        optimizer = AdamW(self.parameters(), lr=self.hparams.lr)
        num_training_steps = self.trainer.estimated_stepping_batches
        num_warmup_steps = num_training_steps // self.trainer.max_epochs // 5
        scheduler = linear_schedule_with_warmup(optimizer=optimizer, 
                                                num_training_steps=num_training_steps,
                                                num_warmup_steps=num_warmup_steps)
        return {"optimizer": optimizer, "lr_scheduler": {"interval": "step", "scheduler": scheduler}}
    
    
    def predict(self, text: str, device: str = 'cpu'):
        self.eval()
        self.freeze()
        self.to(device)
        tokens = self.hparams.tokenizer(text)[0]
        input_ids = torch.tensor(tokens.ids).unsqueeze(0).to(device)
        outputs = self(input_ids=input_ids.to(self.device))
        bio_tags = [self.hparams.id2bio[id] for id in outputs[0].tolist()]
        return ner_post_process(labels=bio_tags, tokens=tokens)
    
    
    def save_label_dict(self, save_path: str):
        with open(save_path, 'w') as f:
            json.dump(self.hparams.id2bio, f)
    
    
    def to_onnx(self, 
                save_path: str,
                embedding_save_path: Optional[str] = None,
                max_length: int = 32,
                input_name: str = 'input', 
                output_name: str = 'output', 
                opset_version: int = 14,
                split_crf: bool = True) -> None:
        self.eval()
        self.freeze()
        text = "好" * max_length
        batch_tokens = self.hparams.tokenizer(text)
        input_ids = [tokens.ids for tokens in batch_tokens]
        input_ids = torch.tensor(input_ids)
        if split_crf:
            with torch.no_grad():
                logits = self.embeddings(input_ids)
                torch.onnx.export(self.classifier, 
                                logits, 
                                save_path, 
                                opset_version=opset_version,
                                input_names=[input_name], 
                                output_names=[output_name],
                                dynamic_axes={input_name: {0: 'batch_sizel', 1: 'seq_length'}, output_name: {0: 'batch_size', 1: 'seq_length'}})
                # 更改形状的最后一维为标签大小, 不然端侧模型会报错
                ner_model = onnx.load(str(save_path)) 
                ner_model.graph.input[0].type.tensor_type.shape.dim[1].dim_value  = max_length
                ner_model.graph.output[0].type.tensor_type.shape.dim[2].dim_value  = len(self.hparams.id2bio)
                onnx.save(ner_model, save_path)
                
                torch.onnx.export(
                    self.embeddings,
                    input_ids,
                    embedding_save_path,
                    opset_version=opset_version,
                    input_names=[input_name],
                    output_names=[output_name],
                    dynamic_axes={input_name: {0: 'batch_size', 1: 'seq_len'}}
                )
        else:
            with torch.no_grad():
                torch.onnx.export(self, 
                                input_ids, 
                                save_path, 
                                opset_version=opset_version,
                                input_names=[input_name], 
                                output_names=[output_name],
                                # dynamic_axes={input_name: {0: 'batch_size', 1: 'seq_len'}, output_name: {0: 'batch_size', 1: 'seq_len'}})
                                dynamic_axes={input_name: {0: 'batch_size'}, output_name: {0: 'batch_size', 1: 'seq_length'}})