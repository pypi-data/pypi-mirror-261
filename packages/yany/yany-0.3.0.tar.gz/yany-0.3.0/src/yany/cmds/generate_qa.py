import os
import re
import json
from .generate_base import GenerateBase
from openai import AsyncOpenAI
from tqdm import tqdm
import asyncio
import pandas as pd
import uuid
import importlib
from datetime import datetime

API_BASE = "https://api.listenai.com/v1"


def checklen(text, max_length=8000):
    total_length = len(text)
    while total_length > max_length:
        removed_length = len(text.pop(0)["content"])
        total_length -= removed_length
    return text


def is_valid_uuid(uuid_to_test, version=4):
    """
    检查 uuid_to_test 是否为有效的UUID字符串。

    参数:
    uuid_to_test (str): 需要检查的字符串。
    version (int): UUID的版本，通常是4。有效值是1、2、3、4、5。

    返回:
    bool: 如果uuid_to_test是有效的UUID，则为True，否则为False。
    """
    try:
        uuid_obj = uuid.UUID(uuid_to_test, version=version)
        # 确保uuid_to_test没有额外的字符，且与生成的UUID相匹配。
        return str(uuid_obj) == uuid_to_test
    except ValueError:
        return False


class GenerateQA(GenerateBase):
    def on_init(self):
        if not is_valid_uuid(os.environ.get("XINGHUO_API_KEY")):
            print("请正确设置 API KEY, 在 .env 里面设置或者直接设置环境变量 XINGHUO_API_KEY")
            exit()
        self.client = AsyncOpenAI(
            api_key=os.environ.get("XINGHUO_API_KEY"),
            base_url=os.environ.get("XINGHUO_API_BASE") or API_BASE
        )
        self.validate = self.get_validate("helper.py")

    def get_validate(self, helper_file):
        if os.path.exists(helper_file):
            spec = importlib.util.spec_from_file_location(
                "helper", helper_file)
            helper = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(helper)
            if hasattr(helper, 'validate'):
                return helper.validate
            else:
                return lambda c: True

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
            '.', 'target/data_exception.xlsx')
        parser.add_argument('--data_exception', '-e', type=str, default=default_data_exception,
                            help=f'data_exception.xlsx 输出的路径，默认为：{default_data_exception}')
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
        try:
            with open(qa_data, "r", encoding="utf-8") as f:
                lines = f.readlines()
                if lines:
                    last_line = lines[-1]
                    last_qa = json.loads(last_line)
                    start_index = last_qa["index"] + 1
                else:
                    start_index = 0
        except FileNotFoundError:
            # If the file doesn't exist, start from the beginning
            start_index = 0

        settings_df = pd.read_excel(data_input, sheet_name='Settings')
        prompt_template = settings_df.iloc[0, 0]

        prompts_df = pd.read_excel(data_input, sheet_name='Prompts')

        df_template = pd.DataFrame({'Template': [prompt_template]})

        current_time = datetime.now()
        time_stamp = current_time.strftime("%Y%m%d-%H%M%S")

        file_name_prefix = os.path.splitext(
            os.path.basename(exception_data))[0]
        base_path = os.path.dirname(exception_data)

        file_name = f"{file_name_prefix}.{time_stamp}.xlsx"
        full_save_path = os.path.join(base_path, file_name)

        file_name_jsonl = f"{file_name_prefix}.{time_stamp}.jsonl"
        full_save_jsonl_path = os.path.join(base_path, file_name_jsonl)

        exception_rows = []

        try:
            for index, row in tqdm(prompts_df.iterrows(), total=len(prompts_df)):
                if index < start_index:
                    continue
                sentence = prompt_template.format(
                    attr=row["attr"], input=row["input"], target=row["target"])
                answer = await self.request(sentence)
                # 如果出现异常，保存数据以便重新处理
                if answer == "" or not self.validate(answer):
                    exception_rows.append(row)
                    if answer:
                        qa = {"input": row["input"],
                              "target": answer, "index": index}
                        with open(full_save_jsonl_path, "a", encoding="utf-8") as exception_f:
                            exception_f.write(json.dumps(
                                qa, ensure_ascii=False) + "\n")
                else:
                    qa = {"input": row["input"],
                          "target": answer, "index": index}
                    with open(qa_data, "a", encoding="utf-8") as qa_data_f:
                        # 追加保存数据
                        qa_data_f.write(json.dumps(
                            qa, ensure_ascii=False) + "\n")
        finally:
            if exception_rows:

                with pd.ExcelWriter(full_save_path, engine='openpyxl') as writer:
                    df_template.to_excel(
                        writer, sheet_name='Settings', index=False)
                    df_data = pd.DataFrame(
                        exception_rows, columns=['input', 'target', 'attr'])
                    df_data.to_excel(
                        writer, sheet_name='Prompts', index=False)

    def run(self, args):
        # 输入数据路径
        data_input = args.input_file
        # 异常数据保存
        exception_data = args.data_exception
        # 生成的数据
        qa_data = args.output
        asyncio.run(self.fetch_qa(data_input, exception_data, qa_data))
