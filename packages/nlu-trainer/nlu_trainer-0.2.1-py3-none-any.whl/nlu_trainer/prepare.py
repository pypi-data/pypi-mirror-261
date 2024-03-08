from pathlib import Path
from wasabi import msg
from nlp_data import NLUDocList, NLUDocStore
from typing import Optional
from random import choices
import os
import pandas as pd
from .utils import print_config, get_lang_from_dir_name, get_domain_from_dir_name, get_tokenizer
from ._config import Config
import shutil


class Prepare():
    def __init__(self, 
                 corpus_dir: str = 'corpus', 
                 dataset_dir: str = 'dataset',
                 pos_file: str = 'positive.txt',
                 neg_file: str = 'negative.txt',
                 pos_extra: str = 'pos_extra.txt', 
                 neg_extra: str = 'neg_extra.txt',
                 pos_label: str = '__label__1#',
                 neg_label: str = '__label__0#',
                 domain_dataset: str = 'domain.txt',
                 intention_dataset: str = 'intention.txt',
                 ner_dataset: str = 'ner',
                 ner_processed_dataset: str = 'ner_processed'):
        """数据准备

        Args:
            corpus_dir: 语料目录,包含abnf,以及正负语料文件等.
            dataset_dir: 数据集目录,包含ner,intention,domain数据集.
            test_dir: 测试目录,包含domain,intention,ner测试数据文件.
            pos_file: 领域正例文件名称.
            neg_file: 领域反例文件名称.
            pos_extra: 领域正例额外文件名称.
            neg_extra: 领域反例额外文件名称.
            pos_label: 领域正例标签.
            neg_label: 领域反例标签.
            domain_dataset: 领域数据集文件名称.
            intention_dataset: 意图数据集文件名称.
            ner_dataset: ner数据集文件名称.
        """
        super().__init__()
        self.corpus_dir = Path(corpus_dir)
        if not self.corpus_dir.exists():
            self.corpus_dir.mkdir(parents=True)
        self.pos_extra = Path(self.corpus_dir, pos_extra)
        if not self.pos_extra.exists():
            self.pos_extra.touch()
        self.neg_extra = Path(self.corpus_dir, neg_extra)
        if not self.neg_extra.exists():
            self.neg_extra.touch()
        self.pos_file = Path(self.corpus_dir, pos_file)
        if not self.pos_file.exists():
            self.pos_file.touch()
        self.neg_file = Path(self.corpus_dir, neg_file)
        if not self.neg_file.exists():
            self.neg_file.touch()
        self.pos_label = pos_label
        self.neg_label = neg_label
        self.abnf_out_dir = Path(corpus_dir) / 'abnf' / 'out'
        if not self.abnf_out_dir.exists():
            self.abnf_out_dir.mkdir(parents=True)
        self.abnf_dir = Path(corpus_dir) / 'abnf'
        self.dataset_dir = Path(dataset_dir)
        self.domain_dataset = Path(dataset_dir, domain_dataset)
        self.intention_dataset = Path(dataset_dir, intention_dataset)
        self.ner_dataset = Path(dataset_dir, ner_dataset)
        self.ner_processed_dataset = Path(dataset_dir, ner_processed_dataset)
        self.store = NLUDocStore
        self.lang = get_lang_from_dir_name()
        if self.lang in Config.EN:
            self.store.bucket_name = 'nlu-en' 
        self.domain = get_domain_from_dir_name()
        # 获取默认tokenizer,用于生成数据集之前的预处理,预处理时候不会填充
        self.tokenizer = get_tokenizer(lang=self.lang, max_length=100, pad_side='right')
        
        
    def docs(self, num_docs: int = 5000, parse: bool = True, push: bool = True):
        """准备文档数据,并推送到nlp-data

        Args:
            num_docs (int): 生成的文档数量。
            parse (bool, optional): 是否分析文档. Defaults to True.
            push (bool, optional): 是否推送. Defaults to True.
        """
        print_config(locals())
        if self.abnf_out_dir.exists():
            for file in self.abnf_out_dir.iterdir():
                file.unlink()
            self.abnf_out_dir.rmdir()
        os.system(f"cd {str(self.abnf_dir)} && bash run.sh . {num_docs}")
        add_space = True if (self.lang in Config.EN) else False
        docs = NLUDocList.from_abnf_output(abnf_output_dir=self.abnf_out_dir, domain=self.domain, add_space=add_space)
        docs.set_language(self.lang)
        if parse:
            # 分析意图标签数量
            intention_labels = set([intention.text for intention in docs.intention])
            intention_labels = {label: 0 for label in intention_labels}
            # 统计标签数量
            for intention in docs.intention:
                intention_labels[intention.text] += 1
            msg.info(f"所有意图标签数量: {len(intention_labels)}")
            all_intention_labels = [item for item in intention_labels.items()]
            intention_df = pd.DataFrame.from_records(all_intention_labels,columns=['标签', '数量'])
            # 分析意图标签数量
            intention_mean = int(intention_df['数量'].mean())
            msg.info(f"当前意图标签数量均值: {intention_mean}")
            intention_dis = abs(intention_df['数量'] - intention_mean).mean()
            intention_top = int(intention_mean + intention_dis)
            intention_bottom = int(intention_mean - intention_dis)
            # 暂时不对数据量太多的意图进行提示
            # upper_df = intention_df[intention_df['数量']>intention_top]
            # for i, row in upper_df.iterrows():
            #     msg.warn(f"意图{row['标签']}: 当前{row['数量']}条, 数量过多")
            lower_df = intention_df[intention_df['数量']<intention_bottom]
            for i, row in lower_df.iterrows():
                msg.warn(f"意图{row['标签']}: 当前{row['数量']}条, 数量过少")
            if len(lower_df) == 0:
                msg.good(f"意图标签数据分布正常")
            # 分析实体标签数量
            all_slot_labels = [slot.label for slots in docs.slots if slots is not None for slot in slots]
            slot_labels = set(all_slot_labels)
            slot_labels = {label: 0 for label in slot_labels}
            for slot in all_slot_labels:
                slot_labels[slot] += 1
            msg.info(f"所有实体标签数量: {len(slot_labels)}")
            all_slot_labels = [item for item in slot_labels.items()]
            slot_df = pd.DataFrame.from_records(all_slot_labels,columns=['标签', '数量'])
            slot_mean = int(slot_df['数量'].mean())
            msg.info(f"当前实体标签数量均值: {slot_mean}")
            slot_dis = abs(slot_df['数量'] - slot_mean).mean()
            slot_top = int(slot_mean + 3 * slot_dis)
            slot_bottom = int(slot_mean - 3 * slot_dis)
            # upper_df = slot_df[slot_df['数量']>slot_top]
            # for i, row in upper_df.iterrows():
            #     msg.warn(f"实体{row['标签']}: 当前{row['数量']}条, 数量过多")
            lower_df = slot_df[slot_df['数量']<slot_bottom]
            for i, row in lower_df.iterrows():
                msg.warn(f"实体{row['标签']}: 当前{row['数量']}条, 数量过少")
            if len(lower_df) == 0:
                msg.good(f"各类实体数据分布正常")
        if push:
            # 推送到nlp-data
            doc_save_name = self.domain + '/train'
            all_doc_names = self.store.list(show_table=False)
            if doc_save_name in all_doc_names:
                msg.warn("已存在同名文档,将覆盖")
            self.store.push(docs=docs, name=doc_save_name)
            msg.info(f"已推送到nlp-data: {doc_save_name}, 可通过命令行查看: nlp-data list --bucket {self.store.bucket_name}")
        
        
    def corpus(self, num_choices: Optional[int] = None):
        """准备domain正负向数据,将nlp-data领域数据作为正向,其他领域数据作为负向

        Args:
            num_docs (int): 生成文档数量.
            num_choices (Optional[int], optional): 负向每个领域的数量. 默认为None,此时将按照正向领域数量的2倍作为负向领域数量.
        """
        print_config(locals())
        msg.info(f"prepare corpus for domain: {self.domain}, from bucket {self.store.bucket_name}")
        # 首先删除原有文件
        if self.neg_file.exists():
            self.neg_file.unlink()
        if self.pos_file.exists():
            self.pos_file.unlink()
        domain = self.domain
        # 获取所有文档名称  
        all_doc_names = self.store.list(show_table=False)
        neg_doc_names = set([doc.split('/')[0] for doc in all_doc_names if domain not in doc])
        pos_doc_names = set([doc.split('/')[0] for doc in all_doc_names if domain in doc])
        num_domain = len(pos_doc_names) + len(neg_doc_names)
        
        # 保存正向数据
        pos_docs = NLUDocList()
        for pos_doc_name in pos_doc_names:
            train_pos_doc_name = pos_doc_name + '/train'
            if train_pos_doc_name in all_doc_names:
                docs = self.store.pull(name=train_pos_doc_name)
                pos_docs.extend(docs)
            test_pos_doc_name = pos_doc_name + '/test'
            if test_pos_doc_name in all_doc_names:
                docs = self.store.pull(name=test_pos_doc_name)
                pos_docs.extend(docs)
        with open(self.pos_file, 'a', encoding='utf-8') as f:
            for doc in pos_docs:
                f.write(doc.text+'\n')
        msg.good(f'已保存{len(pos_docs)}条正例')
        
        # 计算每个领域的反例数量
        if not num_choices:
            num_choices = (2 * len(pos_docs)) // (num_domain - len(pos_doc_names))
            msg.info(f'每个领域的反例数量为2 * {len(pos_docs)} / ({num_domain} - {len(pos_doc_names)}) = {num_choices}')
        else:
            msg.info(f'每个领域的反例数量为{num_choices}')
        # 保存负向数据
        for neg_doc_name in neg_doc_names:
            neg_docs = NLUDocList()
            train_neg_doc = neg_doc_name + '/train'
            if train_neg_doc in all_doc_names:
                docs = self.store.pull(train_neg_doc)
                neg_docs.extend(docs=docs)
            test_neg_doc = neg_doc_name + '/test'
            if test_neg_doc in all_doc_names:
                docs = self.store.pull(test_neg_doc)
                neg_docs.extend(docs=docs)
            # 如果意图中没有none,则按照意图进行采样
            if None not in neg_docs.intention:
                neg_docs = neg_docs.sample_by_intention(n_sample=num_choices)
            else:
                neg_docs = choices(neg_docs, k=num_choices)
            with open(self.neg_file, 'a', encoding='utf-8') as f:
                for doc in neg_docs:
                    f.write(doc.text)
            msg.good(f'已保存{neg_doc_name}的{num_choices}条反例')
            
    def dataset(self, up_sample: bool = False, domain: bool = True, intention: bool = True, ner: bool = True):
        """准备数据集,领域数据集会添加pos_extra和neg_extra的数据
        
        Args:
            up_sample (bool, optional): 是否对意图数据集进行上采样. Defaults to False.
            domain (bool, optional): 是否保存领域数据集. Defaults to True.
            intention (bool, optional): 是否保存意图数据集. Defaults to True.
            ner (bool, optional): 是否保存ner数据集. Defaults to True.
        """
        print_config(locals())
        
        domain_name = self.domain
        docs: NLUDocList = self.store.pull(domain_name + '/train')
        
        # 保存意图数据集
        if intention or ner:
            # 如果需要上采样,则进行上采样
            if up_sample:
                pre_num = len(docs)
                with msg.loading(f"正在根据意图数量上采样文档..."):
                    docs = docs.up_sampling_by_intention()
                msg.good(f"已上采样文档: {pre_num} -> {len(docs)}")   
                
            if ner:
                dsd = docs.convert_slots_to_ner_dataset()
                if self.ner_dataset.exists():
                    shutil.rmtree(self.ner_dataset)
                # 删除处理之前的数据集
                if self.ner_processed_dataset.exists():
                    shutil.rmtree(self.ner_processed_dataset)
                dsd.save_to_disk(self.ner_dataset)
                msg.good(f"NER数据集已保存至{self.ner_dataset}")
                
            if intention:
                if self.lang in Config.EN:
                    for doc in docs:
                        tokens = self.tokenizer(doc.text, padding=False)[0]
                        doc.text = ' '.join(tokens.text)
                    docs.convert_intention_to_fasttext_dataset(save_path=self.intention_dataset, split_type="no_split")
                else:
                    docs.convert_intention_to_fasttext_dataset(save_path=self.intention_dataset, split_type="char")
                
                msg.good(f"意图数据集已保存至{self.intention_dataset}")
                
        if domain:
            # 保存领域数据集
            if self.domain_dataset.exists():
                self.domain_dataset.unlink()
            with open(self.pos_file, 'r', encoding='utf-8') as f:
                pos_lines = f.readlines()
            with open(self.pos_extra, 'r', encoding='utf-8') as f:
                pos_extra_lines = f.readlines()
                pos_lines += pos_extra_lines
                msg.info(f"正例额外数据数量: {len(pos_extra_lines)}")
            with open(self.neg_file, 'r', encoding='utf-8') as f:
                neg_lines = f.readlines()
            with open(self.neg_extra, 'r', encoding='utf-8') as f:
                neg_extra_lines = f.readlines()
                neg_lines += neg_extra_lines
                msg.info(f"反例额外数据数量: {len(neg_extra_lines)}")
                
            with open(self.domain_dataset, 'a', encoding='utf-8') as f:
                for line in pos_lines:
                    line = line.strip()
                    if line:
                        if self.lang in Config.EN:
                            line = " ".join(self.tokenizer(line, padding=False)[0].text)
                        else:
                            line = " ".join(list(line))
                        f.write(f'{self.pos_label} {line}\n')
                for line in neg_lines:
                    line = line.strip()
                    if line:
                        if self.lang in Config.EN:
                            line = " ".join(self.tokenizer(line, padding=False)[0].text)
                        else:
                            line = " ".join(list(line))
                        f.write(f'{self.neg_label} {line}\n')
            msg.good(f"领域数据集已保存至{self.domain_dataset}")