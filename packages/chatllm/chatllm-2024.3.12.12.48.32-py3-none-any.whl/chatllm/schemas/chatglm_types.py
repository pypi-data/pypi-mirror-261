#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : chatglm_types
# @Time         : 2024/3/11 20:10
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  :

from meutils.pipe import *


class Part(BaseModel):
    id: str
    logic_id: str = ''
    role: str
    content: List[Dict[str, Any]]
    model: str
    recipient: str = ''
    created_at: str
    meta_data: dict
    status: str


class Data(BaseModel):
    """
    {
        "id": "65eef45f3901fe6e0bb7153b",
        "conversation_id": "65eef45e3901fe6e0bb7153a",
        "assistant_id": "65940acff94777010aa6b796",
        "parts": [
            {
                "id": "65eef45f3901fe6e0bb7153b",
                "logic_id": "62a2d941-43ba-4a00-9933-4f2a18979201",
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": "这是我为您创作的可爱猫咪图画，希望您喜欢。",
                        "status": "finish"
                    }
                ],
                "model": "chatglm-all-tools",
                "recipient": "all",
                "created_at": "2024-03-11 20:09:03",
                "meta_data": {
                    "toolCallRecipient": null
                },
                "status": "finish"  #
            }
        ],
        "created_at": "2024-03-11 20:09:03",
        "meta_data": {},
        "status": "finish",
        "last_error": {}
    }

    """
    id: str = "65940acff94777010aa6b796" # chatglm4
    conversation_id: str
    assistant_id: str
    parts: List[Part]
    created_at: str
    meta_data: dict
    status: str
    last_error: dict
