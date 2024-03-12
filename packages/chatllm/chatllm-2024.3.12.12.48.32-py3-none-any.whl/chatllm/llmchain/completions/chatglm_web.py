#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : chatglm_web
# @Time         : 2024/3/11 18:52
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm 🧩 🔨
# @Description  : https://github.com/ikechan8370/chatgpt-plugin/blob/32af7b9a74fdfbd329f5977c6e3fb5b3928ed0f1/client/ChatGLM4Client.js#L6
import httpx

from meutils.pipe import *
from meutils.notice.feishu import send_message
from meutils.str_utils.regular_expression import parse_url

from chatllm.schemas import chatglm_types
from chatllm.schemas.openai_types import chat_completion, chat_completion_chunk
from chatllm.schemas.openai_api_protocol import ChatCompletionRequest
from chatllm.utils.openai_utils import openai_response2sse

from fastapi import UploadFile
from openai.types.file_object import FileObject


class Completions(object):
    def __init__(self, **client_params):
        self.api_key = client_params.get('api_key')
        self.access_token = self.get_access_token(self.api_key)

        self.httpx_client = httpx.Client(headers=self.headers, follow_redirects=True)
        self.httpx_aclient = httpx.AsyncClient(headers=self.headers, follow_redirects=True)

    # def create(self):
    #
    #     self.httpx_client.post(url, json={})

    def create(self, request: Union[dict, ChatCompletionRequest]):

        url = "https://chatglm.cn/chatglm/backend-api/assistant/stream"
        payload = isinstance(request, dict) and request or request.model_dump()
        # response = self.httpx_client.post(url=url, json=payload)
        response: httpx.Response
        with self.httpx_client.stream("POST", url=url, json=payload, timeout=200) as response:

            content = ""
            for chunk in response.iter_lines():
                # yield from self.do_chunk(line)
                # chunk = chatglm_types.Data.parse_obj(chunk)

                for chat_completion_chunk in self.do_chunk(chunk):
                    yield chat_completion_chunk

    def do_chunk(self, chunk):

        if chunk := chunk.strip().strip("event:message\ndata: ").strip():

            # logger.debug(line)
            chunk = chatglm_types.Data.model_validate_json(chunk)
            if chunk.parts and chunk.parts[0].content:

                if chunk.parts[0].role == "assistant" and chunk.parts[0].content[0].get("type") == "text":
                    chat_completion_chunk.choices[0].delta.content = chunk.parts[0].content[0].get("text")
                    yield chat_completion_chunk
                #     print(chat_completion_chunk)
                #
                else:
                    if chunk.parts[0].get("type")=="tool_calls":
                        tool_content = chunk.parts[0].get("tool_calls")

                    chat_completion_chunk.choices[0].delta.content = str(chunk.parts[0].content)
                    yield chat_completion_chunk

                if chunk.status == 'finish':
                    _ = chat_completion_chunk.model_copy(deep=True)
                    _.choices[0].delta.content = ""
                    _.choices[0].finish_reason = "stop"  # 特殊
                    yield _

            # if kimi_data.event == 'cmpl':
            #     chat_completion_chunk.choices[0].delta.content = kimi_data.content
            #     yield chat_completion_chunk
            #
            # if kimi_data.event == 'all_done':
            #     _ = chat_completion_chunk.model_copy(deep=True)
            #     _.choices[0].delta.content = ""
            #     _.choices[0].finish_reason = "stop"  # 特殊
            #     yield _
            #     return

    @property
    def headers(self):
        return {
            'Authorization': f"Bearer {self.access_token}",
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }

    @staticmethod
    @ttl_cache(3600 * 2)
    def get_access_token(refresh_token=None):  # 设计重试
        refresh_token = refresh_token or "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDE0OTU3OCwianRpIjoiYmQ3YWI2ZDItNWViNS00YmVmLTlmMWMtYzU5NTMwM2IyN2ZkIiwidHlwZSI6InJlZnJlc2giLCJzdWIiOiIzNmE4NmM1Yzc2Y2Q0MTcyYTE5NGYxMjQwZTgyMmIwOSIsIm5iZiI6MTcxMDE0OTU3OCwiZXhwIjoxNzI1NzAxNTc4LCJ1aWQiOiI2NDRhM2QwY2JhMjU4NWU5MDQ2MDM5ZGIiLCJ1cGxhdGZvcm0iOiIiLCJyb2xlcyI6WyJ1bmF1dGhlZF91c2VyIl19.gN8ci_OO8Pp0t3wZ3v1lG2X1xoLgGushf3fkm5pRl0M"

        headers = {
            'Authorization': f"Bearer {refresh_token}",
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }
        url = "https://chatglm.cn/chatglm/backend-api/v1/user/refresh"
        response = httpx.post(url, headers=headers)

        # logger.debug(refresh_token)
        # logger.debug(response.text)
        # logger.debug(response.status_code)

        if response.status_code != 200:
            send_message(f"Kimi refresh_token:\n\n{response.text}\n\n{refresh_token}", title="Kimi")
            response.raise_for_status()

        # refresh_token = response.get("refresh_token") # 是否去更新
        return response.json().get("result", {}).get("accessToken")

    def image2markdown(self, image_data: Optional[dict] = None):
        image_data = image_data or {
            'type': 'image',
            'image': [
                {'image_url': 'https://sfile.chatglm.cn/testpath/b36fc572-243b-5fce-8bb7-d1c49bba96fa_0.png'}],
            'status': 'init'
        }

        markdown_string = ''
        if image_data['type'] == 'image':
            for image in image_data['image']:
                markdown_string += f"![image]({image['image_url']})\n"

        return markdown_string


if __name__ == '__main__':
    # print(Completions.get_access_token())

    data = {
        "assistant_id": "65940acff94777010aa6b796",
        "conversation_id": "",
        # "conversation_id": "65efba8b7df88e608802acb1",
        "meta_data": {
            "is_test": False,
            "input_question_type": "xxxx",
            "channel": "",
            "draft_id": ""
        },
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        # "text": "你是一个资深民商事律师，请你运用联网功能，帮我解决以下问题：\n压岁钱的所有权归谁，父母是否有权支配孩子压岁钱？\n请帮我写出相关法条和判例。",
                        "text": "南京今天天气"

                    }
                ]
            },

        ]
    }


    for i in Completions().create(data):
        print(i)
        pass

