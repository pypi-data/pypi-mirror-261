# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ChatMlMessageRole(str, enum.Enum):
    """
    ChatML role (system|assistant|user|function_call)
    """

    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"
    FUNCTION_CALL = "function_call"

    def visit(
        self,
        user: typing.Callable[[], T_Result],
        assistant: typing.Callable[[], T_Result],
        system: typing.Callable[[], T_Result],
        function_call: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChatMlMessageRole.USER:
            return user()
        if self is ChatMlMessageRole.ASSISTANT:
            return assistant()
        if self is ChatMlMessageRole.SYSTEM:
            return system()
        if self is ChatMlMessageRole.FUNCTION_CALL:
            return function_call()
