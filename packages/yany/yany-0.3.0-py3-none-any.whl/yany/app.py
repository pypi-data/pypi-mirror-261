import argparse
import os
from dotenv import load_dotenv

from .cmds import GenerateInit, GenerateQA, GeneratePrompt


def main():
    load_dotenv(os.path.join(os.getcwd(), '.env'))

    parser = argparse.ArgumentParser(description='星火大模型人设工具')
    subparsers = parser.add_subparsers(help='多个指令')

    parser_g = subparsers.add_parser(
        'generate', aliases=['g'], help='生成相关文件或代码')
    subparsers_g = parser_g.add_subparsers(help='prompt 生成请求星火的 prompt 文件')

    GenerateInit(subparsers)

    GeneratePrompt(subparsers_g)
    GenerateQA(subparsers_g)

    args = parser.parse_args()

    # 根据选择的子命令执行对应的函数
    if hasattr(args, 'func'):
        args.func(args)
    else:
        # 如果没有指定子命令，打印帮助信息
        parser.print_help()


if __name__ == '__main__':
    main()
