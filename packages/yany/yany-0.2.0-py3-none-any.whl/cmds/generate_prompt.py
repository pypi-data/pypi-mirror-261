import os
import json
from importlib import resources
from .generate_base import GenerateBase


class GeneratePrompt(GenerateBase):

    def on_init(self):
        self.prompt = """假设你是一个用户可自定义的讯飞星火开源的AI助手，在给定的人设背景下回复用户问题<ret>##人设背景如下：{attr}##用户：{{{input}}}##参考答案：{{{target}}}##回答：{{}}"""

    def add_cli(self):
        parser = self.subparsers.add_parser(
            'prompt', aliases=['p'], help='生成人设修改的 prompt 文件')
        parser.add_argument('--template', '-t', type=str, default=self.get_default_template_path(),
                            help=f'模板文件的路径，默认为：{self.get_default_template_path()}')
        parser.add_argument(
            '--input_file', '-i', type=str, default=self.get_default_input_file(),
            help=f'人设文件的路径，默认为：{self.get_default_input_file()}')

        default_output_path = os.path.join('.', 'target/prompts.txt')
        parser.add_argument('--output', '-o', type=str, default=default_output_path,
                            help=f'prompts.txt 输出的路径，默认为：{default_output_path}')
        parser.set_defaults(func=self.run)

    def get_default_template_path(self):
        """获取默认模板路径"""
        with resources.path('cmds.templates', 'renshe_1000.jsonl') as renshe_1000:
            return renshe_1000

    def get_default_input_file(self):
        return os.path.join('.', 'attribute.json')

    def run(self, args):
        self.attr = json.load(open(args.input_file, "r"))
        self.output = args.output
        assert len(
            self.attr) > 0, "人设文件为空"
        joined_att = '，'.join(
            [f'(你的{key}：{value})' for key, value in self.attr.items()])
        data = open(args.template, "r").readlines()
        with open(self.output, "w") as fw:
            for item in data:
                line = json.loads(item)
                new_line = self.prompt.format(
                    attr=joined_att, input=line["inputs"], target=line["target"])
                fw.write(new_line + "\n")
        print("prompt 已输出到 target/prompts.txt")
