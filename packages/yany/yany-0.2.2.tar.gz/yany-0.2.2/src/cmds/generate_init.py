import os
import shutil
from importlib import resources

from .generate_base import GenerateBase


class GenerateInit(GenerateBase):
    def add_cli(self):
        parser = self.subparsers.add_parser(
            'init', aliases=['new'], help='在当前文件中创建 attribute.json 和 target 目录')
        parser.set_defaults(func=self.run)

    def run(self, args):
        with resources.path('cmds.templates', 'attribute.json') as attribute_path:
            shutil.copy(attribute_path, os.path.join('.', 'attribute.json'))
        with resources.path('cmds.templates', 'env') as attribute_path:
            shutil.copy(attribute_path, os.path.join('.', '.env'))
