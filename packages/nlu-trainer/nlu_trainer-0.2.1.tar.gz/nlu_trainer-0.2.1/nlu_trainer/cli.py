from jsonargparse import CLI 
from .prepare import Prepare
from .train import Train
from .test import Test
from .push import Push
from pathlib import Path
import shutil
from wasabi import msg
from ._config import Config
from typing import Literal
from .utils import check_dir_name

AVALIABLE_LANG = Literal['zho', 'eng', 'cmn']


def init_project(domain: str, lang: AVALIABLE_LANG):
    """在本目录下初始化项目,并生成语料文件,默认模型训练配置文件,默认项目配置文件以及数据文件。

    Args:
        name (str): 项目名称,会在本目录下创建一个同名的文件夹
    """
    project_dir = Path(domain + '_' + lang)
    check_dir_name(project_dir)
    if project_dir.exists():
        msg.fail(f'{project_dir.stem} already exists', exits=1)
    project_dir.mkdir()
    msg.good(f'created project dir {project_dir.absolute()}')
    shutil.copytree(Config.DEFAULT_CORPUS_DIR, project_dir / 'corpus')
    shutil.copytree(Config.DEFAULT_CONFIG_DIR, project_dir / 'configs')
    # 创建模型文件路径
    cloud_model_dir = project_dir / Config.CLOUD_MODEL_DIR
    local_model_dir = project_dir / Config.LOCAL_MODEL_DIR
    if not cloud_model_dir.exists():
        cloud_model_dir.mkdir(parents=True)
    if not local_model_dir.exists():
        local_model_dir.mkdir(parents=True)
    

        
components = {
    "init": init_project,
    "prepare": Prepare,
    "train": Train,
    "test": Test,
    "push": Push
}

def run_cli():
    CLI(components=components, as_positional=False)