from wasabi import msg
from ._config import Config
import os
from pathlib import Path



class Push(object):
    """推送模型到模型保存服务器
    """
    def __init__(self):
        self.exp_file_path: Path = Config.EXP_SCRIPT
        self.project_dir_name = Path('.').resolve().name

    def cloud(self, 
              model_dir: str = '/data/wangshilin/24_push/model_folder',
              password: str = 'pachira123', 
              host: str = '192.168.130.27', 
              user: str = 'wangmengdi'):
        """推送云侧模型到保存目录, 云侧模型保存目录为: /data/wangshilin/24_push/model_folder/项目目录名/cloud/model

        Args:
            model_dir (str, optional): 模型保存的目录. Defaults to '/data/wangshilin/24_push/model_folder'.
            password (str, optional): 密码. Defaults to 'pachira123'.
            host (str, optional): 主机地址. Defaults to '192.168.130.27'.
            user (str, optional): 用户名. Defaults to 'wangmengdi'.
        """
        push_dir = f'{user}@{host}:{model_dir}/{self.project_dir_name}'
        result = os.system(f'expect {self.exp_file_path} {Config.CLOUD_DIR} {push_dir} {password}')
        if result != 0:
            msg.fail('push failed')
        else:
            msg.good(f'pushed {Config.CLOUD_DIR} to {push_dir}')
        
    def local(self,
              model_dir: str = '/data/wangshilin/24_push/model_folder',
              password: str = 'pachira123', 
              host: str = '192.168.130.27',
              user: str = 'wangmengdi'):
        """推送端侧模型到保存目录, 端侧模型保存目录为: /data/wangshilin/24_push/model_folder/项目目录名/local/models

        Args:
            model_dir (str, optional): 模型保存目录. Defaults to '/data/wangshilin/24_push/model_folder'.
            password (str, optional): 密码. Defaults to 'pachira123'.
            host (str, optional): 主机地址. Defaults to '192.168.130.27'.
            user (str, optional): 用户名. Defaults to 'wangmengdi'.
        """
        push_dir = f'{user}@{host}:{model_dir}/{self.project_dir_name}'
        result = os.system(f'expect {self.exp_file_path} {Config.LOCAL_DIR} {push_dir} {password}')
        if result != 0:
            msg.fail('push failed')
        else:
            msg.good(f'pushed {Config.LOCAL_DIR} to {push_dir}')
        
    def all(self,
            model_dir: str = '/data/wangshilin/24_push/model_folder',
            password: str = 'pachira123',
            host: str = '192.168.130.27',
            user: str = 'wangmengdi'):
        """推送端侧和云侧模型到保存目录, 端侧模型保存目录为: /data/wangshilin/24_push/model_folder/项目目录名/local/models, 云侧模型保存目录为: /data/wangshilin/24_push/model_folder/项目目录名/cloud/model

        Args:
            model_dir (str, optional): 模型保存目录. Defaults to '/data/wangshilin/24_push/model_folder'.
            password (str, optional): 密码. Defaults to 'pachira123'.
            host (str, optional): 主机地址. Defaults to '192.168.130.27'.
            user (str, optional): 用户名. Defaults to 'wangmengdi'.
        """
        self.cloud(model_dir, password, host, user)
        self.local(model_dir, password, host, user)
        
        