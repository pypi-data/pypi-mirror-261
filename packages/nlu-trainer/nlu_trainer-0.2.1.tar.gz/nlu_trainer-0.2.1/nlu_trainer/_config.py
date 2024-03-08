from pathlib import Path  
from dataclasses import dataclass


@dataclass
class Config:  
    # 项目默认配置文件目录
    DEFAULT_CONFIG_DIR = Path(__file__).parent / 'configs'
    # 项目默认语料文件目录
    DEFAULT_CORPUS_DIR = Path(__file__).parent / 'corpus'
    # 推送exp脚本文件路径
    EXP_SCRIPT = Path(__file__).parent / 'push.exp'
    
    # [language]
    ZH = ['zho', 'cmn']
    EN = ['eng']

    # [domain]
    # 项目默认fasttext正样本标签
    POS_LABEL: str = '1'
    # 项目默认fasttext负样本标签
    NEG_LABEL: str = '0'
    # domain 额外正样本文件名称,用于修复正样本bug以及测试
    POS_EXTRA: Path = Path('corpus', 'pos_extra.txt')
    # domain 额外负样本文件名称,用于修复负样本bug以及测试
    NEG_EXTRA: Path = Path('corpus', 'neg_extra.txt')

    # [intention]
    LABEL_PREFIX: str = '__label__'


    # [PATH]
    CLOUD_DIR = Path('checkpoints', 'cloud')
    # 云侧模型文件目录
    CLOUD_MODEL_DIR = Path('checkpoints', 'cloud', 'model')
    # 云侧nlu配置文件
    CLOUD_CONFIG_PATH = Path('checkpoints', 'cloud', 'model', 'config.cfg')
    # 云侧领域模型文件目录
    CLOUD_DOMAIN_DIR = Path('checkpoints', 'cloud', 'model', 'domain')
    # 云侧领域模型文件路径
    CLOUD_DOMAIN_MODEL = Path('checkpoints', 'cloud', 'model', 'domain', 'model.bin')
    # 云侧意图模型文件目录
    CLOUD_INTENTION_DIR = Path('checkpoints', 'cloud', 'model', 'intention')
    # 云侧意图模型文件路径
    CLOUD_INTENTION_MODEL = Path('checkpoints', 'cloud', 'model', 'intention', 'model.bin')
    # 云侧ner模型文件目录
    CLOUD_NER_DIR = Path('checkpoints', 'cloud', 'model', 'ner')
    # 云侧ner模型文件路径
    CLOUD_NER_MODEL = Path('checkpoints', 'cloud', 'model', 'ner', 'model.onnx')
    # 云侧词表文件
    CLOUD_VOCAB_PATH = Path('checkpoints', 'cloud', 'model', 'ner', 'word2id.json')
    # 云侧ner标签文件
    CLOUD_LABEL_PATH = Path('checkpoints', 'cloud', 'model', 'ner', 'id2label.json')
    # 端侧文件目录
    LOCAL_DIR = Path('checkpoints', 'local')
    # 端侧模型文件目录
    LOCAL_MODEL_DIR = Path("checkpoints", 'local', 'models')
    # 端侧nlu配置文件
    LOCAL_CONFIG_PATH = Path('checkpoints', 'local', 'models', 'config.cfg')
    # 端侧领域模型文件目录
    LOCAL_DOMAIN_DIR = Path("checkpoints", 'local', 'models', 'domain')
    # 端侧领域模型文件路径
    LOCAL_DOMAIN_MODEL = Path("checkpoints", 'local', 'models', 'domain', 'model.bin')
    # 端侧意图模型文件目录
    LOCAL_INTENTION_DIR = Path("checkpoints", 'local', 'models', 'intention')
    # 端侧意图模型文件路径
    LOCAL_INTENTION_MODEL = Path("checkpoints", 'local', 'models', 'intention', 'model.bin')
    # 端侧embedding模型文件路径
    LOCAL_EMBEDDING_MODEL = Path('checkpoints', 'local', 'embedding.onnx')
    # 端侧ner模型文件目录
    LOCAL_NER_DIR = Path("checkpoints", 'local', 'models', 'ner')
    # 端侧ner模型文件路径
    LOCAL_NER_MODEL = Path("checkpoints", 'local', 'models', 'ner', 'model.onnx')
    # 端侧词表文件
    LOCAL_VOCAB_PATH = Path('checkpoints', 'local', 'models', 'ner', 'word2id.json')
    # 端侧ner标签文件
    LOCAL_LABEL_PATH = Path('checkpoints', 'local', 'models', 'ner', 'id2label.json')


    # [train]

    # [dataset]
    DOMAIN_DATASET = Path('dataset', 'domain.txt')
    INTENTION_DATASET = Path('dataset', 'intention.txt')
    NER_DATASET = Path('dataset', 'ner')
    NER_PROCESSED_DATASET = Path('dataset', 'ner_processed')
    
    # [embedding]
    EN_EMBEDDING: str = 'glove-en-300d-20k'
    ZH_EMBEDDING: str = 'common-300d'
    
