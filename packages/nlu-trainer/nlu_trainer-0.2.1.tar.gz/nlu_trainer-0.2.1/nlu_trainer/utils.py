from typing import List, Tuple, Optional, Literal, Union, Dict
from nlp_data import NLUDocStore, EmbeddingDocStore, EmbeddingDocList
from nlu_inference.tokenizer import CharTokenizer, WordTokenizer, Tokenizer
import rich
import rich.tree
import rich.syntax
from pathlib import Path
from ._config import Config
from nlu_inference.config import Config as NLUConfig


def check_domain_exist_in_bucket(domain: str) -> bool:
    """检查领域是否存在

    Args:
        domain (str): 领域名称.

    Returns:
        bool: 是否存在.
    """
    doc_save_name = domain + '/train'
    all_doc_names = NLUDocStore.list(show_table=False)
    if doc_save_name in all_doc_names:
        return True
    else:
        return False
    
    

def print_config(config: dict):
    """打印配置文件

    Args:
        config (dict): 配置文件.
    """
    style = 'dim'
    tree = rich.tree.Tree("CONFIG", style=style, guide_style=style)
    if 'self' in config:
        config.pop('self')
    for k, v in config.items():
        if k == 'kwargs':
            for k1, v1 in v.items():
                branch = tree.add(k1)
                branch.add(rich.syntax.Syntax(str(v1), "yaml"))
        else:
            branch = tree.add(k)
            branch.add(rich.syntax.Syntax(str(v), "yaml"))
    rich.print(tree)
    


def get_tokenizer(lang: Literal['zho', 'eng', 'cmn'], 
                  max_length: int = 32, 
                  pad_side: Literal['left', 'right'] = 'left',
                  **kwargs) -> Tokenizer:
    """根据语种获取默认分词器

    Args:
        lang (Literal[&#39;zh&#39;, &#39;en&#39;]): 语种
        vocab_path (Union[str, Path, Dict[str, int]]): 词表路径或者词表字典.
        max_length (int, optional): 最大token长度. Defaults to 32.
        pad_side (Literal[&#39;left&#39;, &#39;right&#39;], optional): 填充方式. Defaults to 'left'.
    """
    embedding_name = get_default_embedding_name(lang=lang)
    embedings: EmbeddingDocList = EmbeddingDocStore.pull(embedding_name, show_progress=False)
    vocab = embedings.get_vocab()
    if lang in Config.ZH:
        return CharTokenizer(vocab=vocab, max_length=max_length, pad_side=pad_side)
    if lang in Config.EN:
        return WordTokenizer(vocab=vocab, max_length=max_length, pad_side=pad_side)
    else:
        raise ValueError(f'unknow language {lang}')
    
    
def get_default_embedding_name(lang: Literal['zho', 'eng', 'cmn']) -> str:
    """获取默认embedding名称

    Args:
        lang (str): 语种.

    Returns:
        str: embedding名称.
    """
    if lang in Config.ZH:
        return Config.ZH_EMBEDDING
    if lang in Config.EN:
        return Config.EN_EMBEDDING
    else:
        raise ValueError(f'unknow language {lang}')
    
    
def get_lang_from_dir_name() -> str:
    """从目录名获取语种

    Args:
        dir_name (str): 目录名.

    Returns:
        str: 语种.
    """
    dir_name = Path.cwd().stem
    lang = dir_name.split('_')[-1]
    return lang
    
    
def get_domain_from_dir_name() -> str:
    """从目录名获取领域

    Args:
        dir_name (str): 目录名.

    Returns:
        str: 领域.
    """
    dir_name = Path.cwd().stem
    splits = dir_name.split('_')
    assert len(splits) == 2, f'文件夹名字不符合规范,请使用领域_语种的格式,比如weather_zho, time-query_eng'
    return splits[0]


def check_dir_name(dir: Path):
    """检查目录名是否符合规范

    Args:
        dir (Path): 目录.
    """
    dir_name = dir.stem
    splits = dir_name.split('_')
    if len(splits) != 2:
        raise ValueError(f'文件夹名字不符合规范,请使用领域_语种的格式,比如weather_zho, time-query_eng') 
    lang = splits[-1]
    if lang not in Config.ZH and lang not in Config.EN:
        raise ValueError(f"unknow language {lang}, available language is {Config.ZH} and {Config.EN}") 
    
def get_default_tokenizer_type(lang: str = Literal['zho', 'cmn', 'eng']):
    """获取默认分词器类型

    Returns:
        str: 分词器类型.
    """
    if lang in Config.ZH:
        return 'char'
    if lang in Config.EN:
        return 'word'
    else:
        raise ValueError(f'unknow language {lang}')
    
    
def get_default_nlu_config(max_length: int = 32,
                           pad_side: Literal['left', 'right'] = 'left',
                           pad_id: int = 0,
                           unk_token: str = "UNK",
                           is_cloud: bool = True):
    """获取默认nlu配置
    """
    lang = get_lang_from_dir_name()
    domain = get_domain_from_dir_name()
    tokenizer_type = get_default_tokenizer_type(lang)
    config_str = """
    [nlu]
    @languages = cmn
    domain = "schedule"

    [nlu.domain_inference]
    @inferences = "domain.fasttext"
    model_path = ${path.domain}

    [nlu.intention_inference]
    @inferences = "intention.fasttext"
    model_path = ${path.intention}

    [nlu.ner_inference]
    @inferences = "ner.onnx.cloud"
    model_path = ${path.ner}
    label_path = ${path.label}

    [nlu.tokenizer]
    @tokenizers = "char"
    max_length = 32
    vocab = ${path.vocab}
    pad_side = "left"
    pad_id = 0
    unk_token = "UNK"

    [path]
    ner = "model/ner/model.onnx"
    vocab = "model/ner/word2id.json"
    label = "model/ner/id2label.json"
    domain = "model/domain/model.bin"
    intention = "model/intention/model.bin"
    """
    overrides = {"nlu.domain": domain, 
                 "nlu.@languages": lang, 
                 "nlu.tokenizer.@tokenizers": tokenizer_type, 
                 "nlu.tokenizer.max_length": max_length, 
                 "nlu.tokenizer.pad_side": pad_side, 
                 "nlu.tokenizer.pad_id": pad_id, 
                 "nlu.tokenizer.unk_token": unk_token}
    if not is_cloud:
        overrides['path.ner'] = "models/ner/model.onnx"
        overrides['path.embedding'] = "embedding.onnx"
        overrides['path.vocab'] = "models/ner/word2id.json"
        overrides['path.label'] = "models/ner/id2label.json"
        overrides['path.domain'] = "models/domain/model.bin"
        overrides['path.intention'] = "models/intention/model.bin"
        overrides['nlu.ner_inference.@inferences'] = 'ner.onnx.local'
        overrides['nlu.ner_inference.embedding_path'] = '${path.embedding}'
        overrides['nlu.ner_inference.model_path'] = '${path.ner}'
        overrides['nlu.ner_inference.label_path'] = '${path.label}'
        
    config = NLUConfig().from_str(config_str, overrides=overrides, interpolate=False)
    return config
        
    