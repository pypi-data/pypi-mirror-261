import os
import re
import json
from .generate_base import GenerateBase
from openai import AsyncOpenAI
from tqdm import tqdm
import asyncio
import pandas as pd


API_BASE = "https://api.listenai.com/v1"


def checklen(text, max_length=8000):
    total_length = len(text)
    while total_length > max_length:
        removed_length = len(text.pop(0)["content"])
        total_length -= removed_length
    return text


class GenerateQA(GenerateBase):
    def on_init(self):
        self.client = AsyncOpenAI(
            api_key=os.environ.get("XINGHUO_API_KEY"),
            base_url=os.environ.get("XINGHUO_API_BASE") or API_BASE
        )

    def add_cli(self):
        parser = self.subparsers.add_parser(
            'qa', help='根据 prompts.txt 来生成训练数据')
        default_input_path = os.path.join('.', 'target/prompts.xlsx')
        parser.add_argument(
            '--input_file', '-i', type=str, default=default_input_path,
            help=f'prompts.xlsx 的路径，默认为：{default_input_path}')

        default_output_path = os.path.join('.', 'target/qa_data.jsonl')
        parser.add_argument('--output', '-o', type=str, default=default_output_path,
                            help=f'qa_data.jsonl 输出的路径，默认为：{default_output_path}')

        default_data_exception = os.path.join(
            '.', 'target/data_exception.jsonl')
        parser.add_argument('--data_exception', '-e', type=str, default=default_data_exception,
                            help=f'data_exception.jsonl 输出的路径，默认为：{default_data_exception}')
        parser.set_defaults(func=self.run)

    async def request(self, content):
        completion = await self.client.chat.completions.create(
            model=os.environ.get("XINGHUO_MODEL") or "spark-general-3.0",
            temperature=float(os.environ.get("XINGHUO_TEMPERATURE") or 0.5),
            max_tokens=int(os.environ.get("XINGHUO_MAX_TOKEN") or 8192),
            messages=[{"role": "user", "content": content}]
        )
        return completion.choices[0].message.content

    async def fetch_qa(self, data_input, exception_data, qa_data):
        settings_df = pd.read_excel(data_input, sheet_name='Settings')
        prompt_template = settings_df.iloc[0, 0]

        prompts_df = pd.read_excel(data_input, sheet_name='Prompts')

        question_list = []
        for index, row in prompts_df.iterrows():
            sentence = prompt_template.format(
                attr=row["attr"], input=row["input"], target=row["target"])
            question_list.append([row['input'], sentence])

        qa_dict = {}
        for q in tqdm(question_list):
            question = checklen(q[1])
            answer = await self.request(question)
            if answer == "":  # 如果出现异常，保存数据以便重新处理
                with open(exception_data, "a", encoding="utf-8") as f:
                    ex = {"Q": q[0], "data": q[1]}
                    f.write(json.dumps(ex, ensure_ascii=False) + "\n")
                continue
            else:
                # 追加保存数据
                with open(qa_data, "a", encoding="utf-8") as f:
                    qa = {"input": q[0], "target": answer}
                    f.write(json.dumps(qa, ensure_ascii=False) + "\n")
                continue

    def run(self, args):
        # 输入数据路径
        data_input = args.input_file
        # 异常数据保存
        exception_data = args.data_exception
        # 生成的数据
        qa_data = args.output
        asyncio.run(self.fetch_qa(data_input, exception_data, qa_data))
