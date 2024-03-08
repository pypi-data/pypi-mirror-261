from pathlib import Path
from fasttext import train_supervised
from wasabi import msg
from .model import CRFForEntityExtraction, EntityExtractionDataModule
from typing import Any, List, Literal, Union, Optional
import lightning as L
from lightning.pytorch.callbacks import ModelCheckpoint, EarlyStopping, RichProgressBar
from lightning.pytorch.loggers import CSVLogger
from datetime import datetime
from ._config import Config
from .utils import print_config, get_default_embedding_name, get_lang_from_dir_name, get_domain_from_dir_name, get_default_nlu_config
import warnings
import onnxruntime as ort
import torch
import torch._dynamo
torch._dynamo.config.suppress_errors = True



class Train():
    """训练云侧和端侧模型
    """
    def __init__(self,
                 local_save_dir: Path = Config.LOCAL_DIR,
                 local_domain_dir: Path = Config.LOCAL_DOMAIN_DIR,
                 local_intention_dir: Path = Config.LOCAL_INTENTION_DIR,
                 local_embedding_path: Path = Config.LOCAL_EMBEDDING_MODEL,
                 local_ner_dir: Path = Config.LOCAL_NER_DIR,
                 cloud_save_dir: Path = Config.CLOUD_DIR,
                 cloud_model_dir: Path = Config.CLOUD_MODEL_DIR,
                 cloud_intention_dir: Path = Config.CLOUD_INTENTION_DIR,
                 cloud_domain_dir: Path = Config.CLOUD_DOMAIN_DIR,
                 cloud_ner_dir: Path = Config.CLOUD_NER_DIR,
                 domain_dataset: Path = Config.DOMAIN_DATASET,
                 intention_dataset: Path = Config.INTENTION_DATASET,
                 ner_dataset: Path = Config.NER_DATASET,
                 processed_ner_dataset: Path = Config.NER_PROCESSED_DATASET,
                 cloud_config_path: Path = Config.CLOUD_CONFIG_PATH,
                 local_config_path: Path = Config.LOCAL_CONFIG_PATH
                 ) -> None:
        super().__init__()
        # Path
        self.local_save_dir = local_save_dir
        self.local_domain_dir = local_domain_dir
        self.local_intention_dir = local_intention_dir
        self.local_ner_dir = local_ner_dir
        self.local_embedding_path = local_embedding_path
        self.cloud_save_dir = cloud_save_dir
        self.cloud_model_dir = cloud_model_dir
        self.cloud_intention_dir = cloud_intention_dir
        self.cloud_domain_dir = cloud_domain_dir
        self.cloud_ner_dir = cloud_ner_dir
        self.cloud_config_path = cloud_config_path
        self.local_config_path = local_config_path
        
        # Dataset
        self.domain_dataset = str(domain_dataset)
        self.intention_dataset = str(intention_dataset)
        self.ner_dataset = ner_dataset
        self.processed_ner_dataset = processed_ner_dataset
        
        self.lang = get_lang_from_dir_name()
        self.domain_name = get_domain_from_dir_name()
        

    def domain(self, 
               epochs: int = 30, 
               lr: float = 0.1, 
               ngrams: int = 2,
               bucket: int = 50000,
               dim: int = 100,
               quantize: bool = True,
               qnorm: bool = False,
               retrain: bool = True,
               retrain_epoch: int = 1,
               cutoff: int = 50000,
               qout: bool = False,
               save_local: bool = True,
               save_cloud: bool = True,
               **kwargs):
        """训练领域二分类模型
        """
        print_config(locals())
        model = train_supervised(self.domain_dataset, 
                                 epoch=epochs, 
                                 lr=lr, 
                                 dim=dim,
                                 wordNgrams=ngrams, 
                                 bucket=bucket,
                                 **kwargs)    
        if quantize:
            with msg.loading(f"正在评估原始模型..."):
                result = model.test(self.domain_dataset)
            msg.info(f"原始模型评估结果 -> 测试数量: {result[0]} 准确率: {round(result[1], 4)} 召回率: {round(result[2], 4)}")
            
            with msg.loading(f"正在量化领域模型"):
                model.quantize(input=self.domain_dataset, 
                               qnorm=qnorm, 
                               retrain=retrain, 
                               epoch=retrain_epoch, 
                               cutoff=cutoff, 
                               qout=qout)   
                
            with msg.loading(f"正在评估量化模型..."):
                quantize_result = model.test(self.domain_dataset)
            msg.info(f"量化模型评估结果 -> 测试数量: {quantize_result[0]} 准确率: {round(quantize_result[1], 4)} 召回率: {round(quantize_result[2], 4)}")
            
            if save_cloud:
                if not self.cloud_domain_dir.exists():
                    self.cloud_domain_dir.mkdir(parents=True)
                model.save_model(str(self.cloud_domain_dir / 'model.bin'))
                msg.good(f"云端领域量化模型保存成功: {self.cloud_domain_dir / 'model.bin'}")
            if save_local:
                if not self.local_domain_dir.exists():
                    self.local_domain_dir.mkdir(parents=True)
                model.save_model(str(self.local_domain_dir / 'model.bin'))
                msg.good(f"本地领域量化模型保存成功: {self.local_domain_dir / 'model.bin'}")
        else:    
            if save_cloud:
                if not self.cloud_domain_dir.exists():
                    self.cloud_domain_dir.mkdir(parents=True)
                model.save_model(str(self.cloud_domain_dir / 'model.bin'))
                msg.good(f"云端领域模型保存成功: {self.cloud_domain_dir / 'model.bin'}")
            if save_local:
                if not self.local_domain_dir.exists():
                    self.local_domain_dir.mkdir(parents=True)
                model.save_model(str(self.local_domain_dir / 'model.bin'))
                msg.good(f"本地领域模型保存成功: {self.local_domain_dir / 'model.bin'}")
    
    
    def intention(self,
                  epochs: int = 30,
                  lr: float = 0.1,
                  ngrams: int = 2,
                  bucket: int = 100000,
                  dim: int = 100,
                  quantize: bool = True,
                  qnorm: bool = False,
                  retrain: bool = True,
                  retrain_epoch: int = 1,
                  cutoff: int = 100000,
                  qout: bool = False,
                  save_cloud: bool = True,
                  save_local: bool = True,
                  **kwargs):
        """训练意图分类模型
        """
        print_config(locals())
        model = train_supervised(self.intention_dataset,
                                 epoch=epochs,
                                 lr=lr,
                                 dim=dim,
                                 wordNgrams=ngrams,
                                 bucket=bucket,
                                 **kwargs)
        if quantize:
            with msg.loading(f"正在评估原始模型..."):
                result = model.test(self.intention_dataset)
            msg.info(f"原始模型评估结果 -> 测试数量: {result[0]} 准确率: {round(result[1], 4)} 召回率: {round(result[2], 4)}")
            
            with msg.loading(f"正在量化意图模型"):
                model.quantize(input=self.intention_dataset,
                               qnorm=qnorm,
                               retrain=retrain,
                               epoch=retrain_epoch,
                               cutoff=cutoff,
                               qout=qout)
            with msg.loading(f"正在评估量化模型..."):
                quantize_result = model.test(self.intention_dataset)
            msg.info(f"量化模型评估结果 -> 测试数量: {quantize_result[0]} 准确率: {round(quantize_result[1], 4)} 召回率: {round(quantize_result[2], 4)}")

            if save_cloud:
                if not self.cloud_intention_dir.exists():
                    self.cloud_intention_dir.mkdir(parents=True)
                model.save_model(str(self.cloud_intention_dir / 'model.bin'))
                msg.good(f"云端意图量化模型保存成功: {self.cloud_intention_dir / 'model.bin'}")
            if save_local:
                if not self.local_intention_dir.exists():
                    self.local_intention_dir.mkdir(parents=True)
                model.save_model(str(self.local_intention_dir / 'model.bin'))
                msg.good(f"本地意图量化模型保存成功: {self.local_intention_dir / 'model.bin'}")
        else:
            if save_cloud:
                if not self.cloud_intention_dir.exists():
                    self.cloud_intention_dir.mkdir(parents=True)
                model.save_model(str(self.cloud_intention_dir / 'model.bin'))
                msg.good(f"云端意图模型保存成功: {self.cloud_intention_dir / 'model.bin'}")
            if save_local:
                if not self.local_intention_dir.exists():
                    self.local_intention_dir.mkdir(parents=True)
                model.save_model(str(self.local_intention_dir / 'model.bin'))
                msg.good(f"本地意图模型保存成功: {self.local_intention_dir / 'model.bin'}")
        
        
    def ner(self, 
            lr: float = 0.001,
            devices: Union[List, int] = [0],
            hidden_size: int = 128,
            max_epochs: int = 10,
            freeze_embedding: bool = True,
            embedding_name: Optional[str] = None,
            batch_size: int = 32,
            max_length: int = 32,
            pad_side: Literal['left', 'right'] = "left",
            num_workers: int = 4,
            patience: int = 3,
            save_cloud: bool = True,
            save_local: bool = True,
            label_save_name: str = 'id2label.json',
            vocab_save_name: str = 'word2id.json',
            ignore_warnings: bool = True,
            optimize: bool = False,
            process_batch_size: int = 5000,
            compile: bool = False):
        """训练ner模型

        Args:
            lr (float, optional): 学习率. Defaults to 0.001.
            devices (Union[List, int], optional): 训练的gpu设备. Defaults to [0].
            hidden_size (int, optional): lstm的隐层温度. Defaults to 128.
            max_epochs (int, optional): 最大训练迭代次数. Defaults to 10.
            freeze_embedding (bool, optional): 是否冻结embedding层. Defaults to True.
            embedding_name (Optional[str], optional): 从nlpdata下载的embedding名称,默认会自动选择. Defaults to None.
            batch_size (int, optional): 训练一个批次的大小. Defaults to 32.
            max_length (int, optional): 一个训练样本的最大token数量. Defaults to 32.
            pad_side (Literal[&#39;left&#39;, &#39;right&#39;], optional): 批次样本填充方式. Defaults to "left".
            num_workers (int, optional): dataloader数据处理进程数. Defaults to 4.
            patience (int, optional): 提早结束训练的条件,当训练的f1分数连续patience次不增加时会停止训练. Defaults to 3.
            save_cloud (bool, optional): 是否保存云侧模型. Defaults to True.
            save_local (bool, optional): 是否保存端侧模型. Defaults to True.
            label_save_name (str, optional): 保存的ner标签文件. Defaults to 'id2label.json'.
            vocab_save_name (str, optional): ner模型embedding对应的词表. Defaults to 'word2id.json'.
            ignore_warnings (bool, optional): 是否忽略提醒. Defaults to True.
            optimize (bool, optional): 是否优化onnx模型. Defaults to False.
            process_batch_size (int, optional): 数据处理的一个批次大小. Defaults to 5000.
            compile (bool, optional): 是否编译模型,成功开启编译的时候会增加训练速度. Defaults to False.
        """
        print_config(locals())
        
        L.seed_everything(42)
        
        if ignore_warnings:
            warnings.filterwarnings("ignore")
        
        early_stoppin = EarlyStopping(monitor='val/f1',
                                      patience=patience, 
                                      mode='max')
        # 日期时间为目录名
        log_dir: Path = Path('logs', 'ner', datetime.now().strftime("%Y-%m-%d-%H-%M"))
        ckpt_dir = log_dir / 'checkpoints'

        ckpt = ModelCheckpoint(dirpath=ckpt_dir, 
                            monitor="val/f1",
                            filename="epoch{epoch}-f1_{val/f1:.3f}", 
                            auto_insert_metric_name=False,
                            mode='max',
                            save_last=False,
                            save_top_k=1)
        rich_bar = RichProgressBar()

        logger = CSVLogger(save_dir=log_dir, name='csv', version='')
        
        trainer = L.Trainer(devices=devices, 
                            max_epochs=max_epochs, 
                            precision='16-mixed',
                            accelerator='gpu', 
                            callbacks=[early_stoppin, ckpt, rich_bar],
                            logger=logger,
                            profiler="simple")
        lang = self.lang
        if not embedding_name:
            embedding_name = get_default_embedding_name(lang)
            msg.info(f"{lang}默认embedding: {embedding_name}")
        
        dm = EntityExtractionDataModule(dataset_path=self.ner_dataset, 
                                        processed_dataset_path=self.processed_ner_dataset,
                                        embedding_name=embedding_name,
                                        batch_size=batch_size,
                                        process_batch_size=process_batch_size,
                                        max_length=max_length,
                                        pad_side=pad_side,
                                        num_workers=num_workers,
                                        lang=lang)
        if trainer.local_rank == 0:
            dm.prepare()
            
        
        model = CRFForEntityExtraction(freeze_embedding=freeze_embedding,
                                       lr=lr,
                                       hidden_size=hidden_size,
                                       **dm.hparams)
        
        if compile:
            model = torch.compile(model=model)
            
        trainer.fit(model=model, datamodule=dm)
        
        if save_cloud:
            if not self.cloud_ner_dir.exists():
                self.cloud_ner_dir.mkdir(parents=True)
            crf_model_path = self.cloud_ner_dir / 'model.onnx'
            model.to_onnx(save_path=crf_model_path, split_crf=False, max_length=max_length)
            model.save_label_dict(self.cloud_ner_dir / label_save_name)
            model.hparams.tokenizer.save_vocab_json(self.cloud_ner_dir / vocab_save_name)
            msg.good(f"云侧ner模型保存成功: {crf_model_path}")
            
            if optimize:
                with msg.loading(f"正在优化onnx模型..."):
                    sess_options = ort.SessionOptions()
                    # Set graph optimization level
                    sess_options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_EXTENDED
                    # To enable model serialization after graph optimization set this
                    sess_options.optimized_model_filepath = str(crf_model_path)
                    session = ort.InferenceSession(crf_model_path, sess_options)
                
            nlu_config = get_default_nlu_config(max_length=max_length, pad_side=pad_side, is_cloud=True)
            nlu_config.to_disk(self.cloud_config_path)
            msg.good(f"云侧nlu配置文件保存成功: {self.cloud_config_path}")
            
        if save_local:
            if not self.local_ner_dir.exists():
                self.local_ner_dir.mkdir(parents=True)
            crf_model_path = self.local_ner_dir / 'model.onnx'
            model.to_onnx(save_path=crf_model_path, split_crf=True, max_length=max_length, embedding_save_path=self.local_embedding_path)
            model.save_label_dict(self.local_ner_dir / label_save_name)
            model.hparams.tokenizer.save_vocab_json(self.local_ner_dir / vocab_save_name)
            msg.good(f"端侧ner模型保存成功: {crf_model_path}")
            
            if optimize:
                with msg.loading(f"正在优化onnx模型..."):
                    sess_options = ort.SessionOptions()
                    # Set graph optimization level
                    sess_options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_EXTENDED
                    # To enable model serialization after graph optimization set this
                    sess_options.optimized_model_filepath = str(crf_model_path)
                    session = ort.InferenceSession(crf_model_path, sess_options)
                
            nlu_config = get_default_nlu_config(max_length=max_length, pad_side=pad_side, is_cloud=False)
            nlu_config.to_disk(self.local_config_path)
            msg.good(f"端侧nlu配置文件保存成功: {self.local_config_path}")