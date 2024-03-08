# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ScenarioInputTypeEnum(str, enum.Enum):
    """
    - `TEXT` - TEXT
    - `CHAT_HISTORY` - CHAT_HISTORY
    """

    TEXT = "TEXT"
    CHAT_HISTORY = "CHAT_HISTORY"

    def visit(self, text: typing.Callable[[], T_Result], chat_history: typing.Callable[[], T_Result]) -> T_Result:
        if self is ScenarioInputTypeEnum.TEXT:
            return text()
        if self is ScenarioInputTypeEnum.CHAT_HISTORY:
            return chat_history()
