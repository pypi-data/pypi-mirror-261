from pathlib import Path
from wasabi import msg
from nlu_inference.inference import FasttextInference, NERInferenceLocal, NERInferenceCloud
from nlu_inference.tokenizer import Tokenizer
from nlu_inference.io import CLSResult, NERResult
from ._config import Config
from nlp_data import NLUDocStore, NLUDocList
from nlp_data.document.nlu import NLUExample, NLUDoc
from typing import Optional, Literal, Union, Dict
from docarray.utils.filter import filter_docs
from .utils import get_tokenizer, get_domain_from_dir_name, get_lang_from_dir_name


def test_domain(domain_inference: FasttextInference, tokenizer: Tokenizer) -> None:
    """测试领域模型
    """
    badcases = []
    with open(Config.POS_EXTRA, 'r') as f:
        pos_lines = f.readlines()
    with open(Config.NEG_EXTRA, 'r') as f:
        neg_lines = f.readlines()
    for line in pos_lines:
        tokens = tokenizer(line, padding=False)[0]
        result: CLSResult = domain_inference(tokens=tokens)
        label = result.label 
        score = result.score
        if label != Config.POS_LABEL:
            msg.fail(f"领域模型badcase: {line} True: {Config.POS_LABEL} Predict: {label} Score: {score}")
            badcases.append(line)
    for line in neg_lines:
        tokens = tokenizer(line, padding=False)[0]
        result = domain_inference(tokens=tokens)
        label = result.label
        score = result.score
        if label != Config.NEG_LABEL:
            msg.fail(f"领域模型badcase: {line} True: {Config.NEG_LABEL} Predict: {label} Score: {score}")
            badcases.append(line)
    if len(badcases) == 0:
        msg.good("领域模型全部测试用例通过")
    else:
        msg.warn(f"领域模型badcase数量: {len(badcases)}")
            
def test_intention(intention_inference: FasttextInference, 
                   docs: NLUDocList,
                   tokenizer: Tokenizer) -> None:
    """测试意图模型
    """
    badcases = []
    for doc in docs:
        tokens = tokenizer(doc.text, padding=False)[0]
        result = intention_inference(tokens=tokens)
        label, score = result.label, result.score
        if label != doc.intention.text:
            msg.fail(f"意图模型badcase: {doc.text} True: {doc.intention.text} Predict: {label} Score: {score}")
            badcases.append(doc.text)
    if len(badcases) == 0:
        msg.good("意图模型全部测试用例通过")
    else:
        msg.warn(f"意图模型badcase数量: {len(badcases)}")
            
def test_ner(ner_inference: NERInferenceCloud, docs: NLUDocList, tokenizer: Tokenizer) -> None:
    badcases = []
    for doc in docs:
        doc: NLUDoc
        tokens = tokenizer(doc.text)[0]
        ner_results: NERResult = ner_inference(tokens=tokens)
        predict_doc = NLUDoc(text=doc.text)
        if len(ner_results) > 0:
            for label, text in ner_results.items():
                predict_doc.set_slot(text=text, label=label)
        example: NLUExample = NLUExample(x=doc, y=predict_doc)
        if example.is_slot_badcase:
            msg.fail(f"ner模型badcase: {doc.text} True: {[(slot.text, slot.label) for slot in doc.slots]} Predict: {[(slot.text, slot.label) for slot in predict_doc.slots]}")
            badcases.append(doc.text)
    if len(badcases) == 0:
        msg.good("ner模型全部测试用例通过")
    else:
        msg.warn(f"ner模型badcase数量: {len(badcases)}")
            
def test_docs(domain: str,
              tokenizer: Tokenizer,
              lang: Literal['zh', 'en'] = 'zh',
              domain_inference: Optional[FasttextInference] = None, 
              intention_inference: Optional[FasttextInference] = None, 
              ner_inference: Optional[NERInferenceLocal] = None) -> None:
    if lang == 'en':
        NLUDocStore.bucket_name = 'nlu-en'
    if domain_inference:
        test_domain(domain_inference, tokenizer=tokenizer)
    if intention_inference or ner_inference:
        all_doc_names = NLUDocStore.list(show_table=False)
        domain_test_doc_name = domain + '/test'
        if domain_test_doc_name not in all_doc_names:
            msg.warn(f"领域{domain}测试集不存在,将跳过意图和实体模型测试")
        else:
            domain_test_docs = NLUDocStore.pull(domain_test_doc_name, show_progress=False)
            if len(domain_test_docs) == 0:
                msg.warn(f"领域{domain}测试集为空")
            if intention_inference:
                test_intention(intention_inference, domain_test_docs, tokenizer=tokenizer)
            if ner_inference:
                test_ner(ner_inference, domain_test_docs, tokenizer=tokenizer)
        

class Test:
    """测试云侧和端侧模型
    """
    def __init__(self,
                 local_domain_path: Path = Config.LOCAL_DOMAIN_MODEL,
                 local_intention_path: Path = Config.LOCAL_INTENTION_MODEL,
                 local_ner_path: Path = Config.LOCAL_NER_MODEL,
                 local_embedding_model_path: Path = Config.LOCAL_EMBEDDING_MODEL,
                 local_vocab_path: Path = Config.LOCAL_VOCAB_PATH,
                 local_label_path: Path = Config.LOCAL_LABEL_PATH,
                 cloud_domain_path: Path = Config.CLOUD_DOMAIN_MODEL,
                 cloud_intention_path: Path = Config.CLOUD_INTENTION_MODEL,
                 cloud_ner_path: Path = Config.CLOUD_NER_MODEL,
                 cloud_vocab_path: Path = Config.CLOUD_VOCAB_PATH,
                 cloud_label_path: Path = Config.CLOUD_LABEL_PATH,
                 ) -> None:
        super().__init__()
        
        self.local_domain_path = Path(local_domain_path)
        self.local_intention_path = Path(local_intention_path)
        self.local_ner_path = Path(local_ner_path)
        self.local_embedding_model_path = Path(local_embedding_model_path)
        self.local_vocab_path = Path(local_vocab_path)
        self.local_label_path = Path(local_label_path)
        self.cloud_domain_path = Path(cloud_domain_path)
        self.cloud_intention_path = Path(cloud_intention_path)
        self.cloud_ner_path = Path(cloud_ner_path)
        self.cloud_vocab_path = Path(cloud_vocab_path)
        self.cloud_label_path = Path(cloud_label_path)
        self.domain = get_domain_from_dir_name()
        self.lang = get_lang_from_dir_name()
        
        
    def local(self, docs:bool = False, max_length: int = 32, pad_side: Literal['left', 'right'] = 'left'):
        """测试本地模型

        Args:
            max_length (int, optional): 最大文本长度,用于ner模型推理. Defaults to 32.
            pad_side (Literal[&#39;left&#39;, &#39;right&#39;], optional): 填充方式. Defaults to 'left'.
        """
        
        tokenizer = get_tokenizer(lang=self.lang, max_length=max_length, pad_side=pad_side)

        if not self.local_domain_path.exists():
            msg.warn(title=f"本地领域模型文件不存在: {self.local_domain_path}")
            domain_inference = None
        else:
            with msg.loading("加载本地领域模型..."):
                domain_inference = FasttextInference(self.local_domain_path)
        if not self.local_intention_path.exists():
            msg.warn(title=f"本地意图模型文件不存在: {self.local_intention_path}")
            intention_inference = None
        else:
            with msg.loading("加载本地意图模型..."):
                intention_inference = FasttextInference(self.local_intention_path)
        if not self.local_ner_path.exists() or not self.local_embedding_model_path.exists() or not self.local_vocab_path.exists() or not self.local_label_path.exists():
            msg.warn(title=f"本地ner模型文件不完整")
            ner_inference = None
        else:
            with msg.loading("加载本地ner模型..."):
                ner_inference = NERInferenceLocal(embedding_path=self.local_embedding_model_path,
                                                  model_path=self.local_ner_path,
                                                  label_path=self.local_label_path)
            
        if domain_inference is not None and intention_inference is not None and ner_inference is not None:
            msg.good(title="本地模型文件完整")
        
        if docs:
            test_docs(domain=self.domain, 
                    domain_inference=domain_inference, 
                    intention_inference=intention_inference, 
                    ner_inference=ner_inference,
                    tokenizer=tokenizer)
        
        while True:
            query = input("请输入测试query (输入q退出): ")
            tokens = tokenizer(query)[0]
            if query == 'q':
                break
            if domain_inference is not None:
                result = domain_inference(tokens=tokens)
                domain_label, score = result.label, result.score
                msg.info(f"Domain: {domain_label}, Score: {round(score, 2)}")
            if intention_inference is not None:
                result = intention_inference(tokens=tokens)
                intention_label, score = result.label, result.score
                msg.info(f"Intention: {intention_label}, Score: {round(score, 2)}")
            if ner_inference is not None:
                ner_result = ner_inference(tokens=tokens)
                msg.info(f"Enities: {ner_result}")
    
    def cloud(self, docs: bool = False, max_length: int = 32, pad_side: Literal['left', 'right'] = 'left'):
        """测试云侧模型

        Args:
            domain (str): 领域名称,用于加载测试docs
            max_length (int, optional): 最大文本长度. Defaults to 32.
            pad_side (Literal[&#39;left&#39;, &#39;right&#39;], optional): 填充方式. Defaults to 'left'.
        """
        
        tokenizer = get_tokenizer(lang=self.lang, max_length=max_length, pad_side=pad_side)

        if not self.cloud_domain_path.exists():
            msg.warn(title=f"云侧领域模型文件不存在: {self.cloud_domain_path}")
            domain_inference = None
        else:
            with msg.loading("加载云侧领域模型..."):
                domain_inference = FasttextInference(self.cloud_domain_path)
        if not self.cloud_intention_path.exists():
            msg.warn(title=f"云侧意图模型文件不存在: {self.cloud_intention_path}")
            intention_inference = None
        else:
            with msg.loading("加载云侧意图模型..."):
                intention_inference = FasttextInference(self.cloud_intention_path)
        if not self.cloud_ner_path.exists() or not self.cloud_vocab_path.exists() or not self.cloud_label_path.exists():
            msg.warn(title=f"云侧ner模型文件不完整")
            ner_inference = None
        else:
            with msg.loading("加载云侧ner模型..."):
                ner_inference = NERInferenceCloud(model_path=self.cloud_ner_path,label_path=self.cloud_label_path)
        if domain_inference is not None and intention_inference is not None and ner_inference is not None:
            msg.good(title="云侧模型文件完整")
        
        if docs:
            test_docs(domain=self.domain, 
                    domain_inference=domain_inference, 
                    intention_inference=intention_inference, 
                    ner_inference=ner_inference,
                    tokenizer=tokenizer)
            
        while True:
            query = input("请输入测试query (输入q退出): ")
            tokens = tokenizer(query)[0]
            if query == 'q':
                break
            if domain_inference is not None:
                domain_result = domain_inference(tokens=tokens)
                domain_label, score = domain_result.label, domain_result.score
                msg.info(f"Domain: {domain_label}, Score: {round(score, 2)}")
            if intention_inference is not None:
                intention_result = intention_inference(tokens=tokens)
                intention_label, score = intention_result.label, intention_result.score
                msg.info(f"Intention: {intention_label}, Score: {round(score, 2)}")
            if ner_inference is not None:
                ner_result = ner_inference(tokens=tokens)
                msg.info(f"Enities: {ner_result}")
                
    def add(self) -> None:
        """添加测试用例

        Args:
            domain (str): 领域名称,将根据其保存测试文件到nlp-data nlu bucket,例如 weather/test
        """
        domain = self.domain
        all_doc_names = NLUDocStore.list(show_table=False)
        train_doc_name = domain + '/train'
        if train_doc_name not in all_doc_names:
            msg.fail(f"领域不存在: {domain}. 请通过运行`nlp-data list --bucket nlu`查看所有领域", exits=True)
        with msg.loading(f"正在解析所有意图和实体标签"):
            train_docs = NLUDocStore.pull(train_doc_name, show_progress=False)
            all_intention_labels = sorted(set([i.text for i in train_docs.intention]))
            all_intention_labels = {i:label for i,label in enumerate(all_intention_labels)}
            all_ent_labels = sorted(set([ent.label for doc in train_docs for ent in doc.slots ]))
            all_ent_labels = {i:label for i,label in enumerate(all_ent_labels)}
        test_doc_name = domain + '/test'
        if test_doc_name not in all_doc_names:
            msg.info("当前测试用例为空")
            test_docs = NLUDocList()
            pre_num_test_docs = 0
        else:
            test_docs = NLUDocStore.pull(name=test_doc_name, show_progress=False)
            pre_num_test_docs = len(test_docs)
            msg.info(f"当前领域{domain}测试用例数量: {len(test_docs)}")
        while True:
            query = input("请输入测试query(输入q退出): ")
            if query == 'q':
                break
            if query in test_docs.text:
                msg.warn(f"`{query}` 该测试用例已存在。继续添加将替换原测试用例")
            new_doc = NLUDoc(text=query)
            intention_label_id = input(f"请选择意图标签(输入数字选择,输入q重新输入.): {all_intention_labels}")
            if intention_label_id == 'q':
                continue
            intention_label_id = int(intention_label_id)
            intention_label = all_intention_labels[intention_label_id]
            new_doc.set_intention(text=intention_label)
            msg.good(f"已选择意图标签: {intention_label}")
            while True:
                ent = input(f"请输入实体文本(输入q退出): ")
                if ent == 'q':
                    break
                if ent not in query:
                    msg.warn(f"实体`{ent}`不存在,请重新输入.")
                    continue
                ent_label_id = input(f"请选择实体标签(输入数字选择): {all_ent_labels}")
                ent_label_id = int(ent_label_id)
                ent_label = all_ent_labels[ent_label_id]
                new_doc.set_slot(text=ent, label=ent_label)
                msg.good(f"已为实体`{ent}`设置{ent_label}标签")
            ensure = input("请确认添加测试用例: 输入`1`确认, 输入其他字符放弃")
            if ensure == '1':
                # 删除已存在的测试用例
                query = {"text": {"$neq": query}}
                result_docs = filter_docs(docs=test_docs, query=query)
                if len(result_docs) < len(test_docs):
                    msg.info(f"已删除原有测试用例")
                result_docs.append(new_doc)
                test_docs = result_docs
                final_num_test_docs = len(test_docs)
                
        with msg.loading(f"正在更新测试用例: {test_doc_name}"):
                _ = NLUDocStore.push(docs=test_docs, name=test_doc_name, show_progress=False)
        msg.good(f"测试用例更新成功: {pre_num_test_docs} -> {final_num_test_docs}")
            
    def delete(self, text: Optional[str] = None) -> None:
        """删除测试用例

        Args:
            text (Optional[str], optional): 测试用例文本. Defaults to None.
        """
        domain = self.domain
        all_doc_names = NLUDocStore.list(show_table=False)
        test_doc_name = domain + '/test'
        if test_doc_name not in all_doc_names:
            msg.fail(f"领域{domain}测试用例不存在", exits=True)
        all_docs = NLUDocStore.pull(name=test_doc_name, show_progress=False)
        if text: 
            query = {"text": {"$neq": text}}
            result_docs = filter_docs(docs=all_docs, query=query)
            if len(result_docs) == len(all_docs):
                msg.warn(f"测试用例`{text}`不存在")
                return
            else:
                NLUDocStore.push(docs=result_docs, name=test_doc_name, show_progress=False)
                msg.good(f"测试用例`{text}`已删除")
        else:
            text = input("请输入要删除的测试用例: ")
            query = {"text": {"$neq": text}}
            result_docs = filter_docs(docs=all_docs, query=query)
            if len(result_docs) == len(all_docs):
                msg.warn(f"测试用例`{text}`不存在")
                return
            else:
                NLUDocStore.push(docs=result_docs, name=test_doc_name, show_progress=False)
                msg.good(f"测试用例`{text}`已删除")
        
    def list(self) -> None:
        """列出测试用例
        """
        domain = self.domain
        all_doc_names = NLUDocStore.list(show_table=False)
        test_doc_name = domain + '/test'
        if test_doc_name not in all_doc_names:
            msg.fail(f"领域{domain}测试用例不存在", exits=True)
        all_docs = NLUDocStore.pull(name=test_doc_name, show_progress=False)
        msg.info(f"领域{domain}测试用例数量: {len(all_docs)}")
        msg.info('-'*50)
        for doc in all_docs:
            msg.info(f"Query: {doc.text}")
            msg.info(f"Intention: {doc.intention.text}")
            msg.info(f"Entities: {[(ent.text, ent.label) for ent in doc.slots]}")
            msg.info('-'*50)
        