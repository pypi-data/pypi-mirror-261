# This file was auto-generated by Fern from our API Definition.

import typing

from .named_tool_choice import NamedToolChoice
from .tool_choice_option import ToolChoiceOption

ChatInputDataToolChoice = typing.Union[ToolChoiceOption, NamedToolChoice]
