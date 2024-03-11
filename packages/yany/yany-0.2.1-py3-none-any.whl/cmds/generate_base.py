import os
from abc import ABC, abstractmethod


class GenerateBase(ABC):
    def __init__(self, subparsers) -> None:
        self.subparsers = subparsers

        self.before_init()
        self.on_init()
        self.add_cli()

    def on_init(self):
        pass

    @abstractmethod
    def add_cli(self):
        pass

    def before_init(self):
        self.create_target_directory()

    def create_target_directory(self):
        target_directory = os.path.join('.', 'target')
        if not os.path.exists(target_directory):
            # 如果目标目录不存在，则创建它
            os.makedirs(target_directory)
            print(f"目录 '{target_directory}' 已创建。")
