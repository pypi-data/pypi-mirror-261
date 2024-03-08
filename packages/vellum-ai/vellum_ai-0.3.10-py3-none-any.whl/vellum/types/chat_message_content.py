# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .array_chat_message_content import ArrayChatMessageContent
from .function_call_chat_message_content import FunctionCallChatMessageContent
from .image_chat_message_content import ImageChatMessageContent
from .string_chat_message_content import StringChatMessageContent


class ChatMessageContent_String(StringChatMessageContent):
    type: typing_extensions.Literal["STRING"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ChatMessageContent_FunctionCall(FunctionCallChatMessageContent):
    type: typing_extensions.Literal["FUNCTION_CALL"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ChatMessageContent_Array(ArrayChatMessageContent):
    type: typing_extensions.Literal["ARRAY"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ChatMessageContent_Image(ImageChatMessageContent):
    type: typing_extensions.Literal["IMAGE"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


ChatMessageContent = typing.Union[
    ChatMessageContent_String, ChatMessageContent_FunctionCall, ChatMessageContent_Array, ChatMessageContent_Image
]
