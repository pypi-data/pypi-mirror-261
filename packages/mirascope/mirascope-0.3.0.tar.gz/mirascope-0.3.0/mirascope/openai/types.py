"""Type classes for interacting with the OpenAI Chat API."""
from typing import Any, Callable, Optional, Type, Union

from httpx import Timeout
from openai import AsyncOpenAI, OpenAI
from openai._types import Body, Headers, Query
from openai.types.chat import (
    ChatCompletion,
    ChatCompletionChunk,
    ChatCompletionMessageToolCall,
    ChatCompletionToolChoiceOptionParam,
)
from openai.types.chat.chat_completion import Choice
from openai.types.chat.chat_completion_chunk import Choice as ChunkChoice
from openai.types.chat.chat_completion_chunk import ChoiceDelta, ChoiceDeltaToolCall
from openai.types.chat.chat_completion_message import ChatCompletionMessage
from openai.types.chat.completion_create_params import ResponseFormat
from pydantic import BaseModel, ConfigDict

from ..base import BaseCallParams
from .tools import OpenAITool


class OpenAIChatCompletion(BaseModel):
    """Convenience wrapper around OpenAI chat completions.

    When using Mirascope's convenience wrappers to interact with OpenAI models via
    `OpenAIChat`, responses using `OpenAIChat.create()` will return a
    `OpenAIChatCompletion`, whereby the implemented properties allow for simpler syntax
    and a convenient developer experience.

    Example:

    ```python
    from mirascope import OpenAIChat

    chat = OpenAIChat()
    response = chat.create("What is 1 + 2?")

    print(response.choices)
    #> [Choice(finish_reason='stop', index=0, logprobs=None,
    #  message=ChatCompletionMessage(content='1 + 2 equals 3.', role='assistant',
    #  function_call=None, tool_calls=None))]

    print(response.message)
    #> ChatCompletionMessage(content='1 + 2 equals 3.', role='assistant',
    #  function_call=None, tool_calls=None)

    print(response.content)
    #> 1 + 2 equals 3.
    ```

    """

    completion: ChatCompletion
    tool_types: Optional[list[Type[OpenAITool]]] = None
    start_time: float  # The start time of the completion in ms
    end_time: float  # The end time of the completion in ms

    @property
    def choices(self) -> list[Choice]:
        """Returns the array of chat completion choices."""
        return self.completion.choices

    @property
    def choice(self) -> Choice:
        """Returns the 0th choice."""
        return self.completion.choices[0]

    @property
    def message(self) -> ChatCompletionMessage:
        """Returns the message of the chat completion for the 0th choice."""
        return self.completion.choices[0].message

    @property
    def content(self) -> Optional[str]:
        """Returns the content of the chat completion for the 0th choice."""
        return self.completion.choices[0].message.content

    @property
    def tool_calls(self) -> Optional[list[ChatCompletionMessageToolCall]]:
        """Returns the tool calls for the 0th choice message."""
        return self.message.tool_calls

    @property
    def tools(self) -> Optional[list[OpenAITool]]:
        """Returns the tools for the 0th choice message.

        Raises:
            ValidationError: if a tool call doesn't match the tool's schema.
        """
        if not self.tool_types or not self.tool_calls:
            return None

        extracted_tools = []
        for tool_call in self.tool_calls:
            for tool_type in self.tool_types:
                if tool_call.function.name == tool_type.__name__:
                    extracted_tools.append(tool_type.from_tool_call(tool_call))
                    break

        return extracted_tools

    @property
    def tool(self) -> Optional[OpenAITool]:
        """Returns the 0th tool for the 0th choice message.

        Raises:
            ValidationError: if the tool call doesn't match the tool's schema.
        """
        if not self.tool_types or not self.tool_calls or len(self.tool_calls) == 0:
            return None

        tool_call = self.tool_calls[0]
        for tool_type in self.tool_types:
            if self.tool_calls[0].function.name == tool_type.__name__:
                return tool_type.from_tool_call(tool_call)

        return None

    def dump(self) -> dict[str, Any]:
        """Dumps the chat completion to a dictionary."""
        return {
            "start_time": self.start_time,
            "end_time": self.end_time,
            "output": self.completion.model_dump(),
        }

    def __str__(self):
        """Returns the contained string content for the 0th choice."""
        return self.content if self.content is not None else ""


class OpenAIChatCompletionChunk(BaseModel):
    """Convenience wrapper around chat completion streaming chunks.

    When using Mirascope's convenience wrappers to interact with OpenAI models via
    `OpenAIChat`, responses using `OpenAIChat.stream()` will return a
    `OpenAIChatCompletionChunk`, whereby the implemented properties allow for simpler
    syntax and a convenient developer experience.

    Example:

    ```python
    from mirascope import OpenAIChat

    chat = OpenAIChat()
    stream = chat.stream("What is 1 + 2?")

    for chunk in stream:
        print(chunk.content)
    #> 1
    #  +
    #  2
    #   equals
    #
    #  3
    #  .
    ```
    """

    chunk: ChatCompletionChunk
    tool_types: Optional[list[Type[OpenAITool]]] = None

    @property
    def choices(self) -> list[ChunkChoice]:
        """Returns the array of chat completion choices."""
        return self.chunk.choices

    @property
    def choice(self) -> ChunkChoice:
        """Returns the 0th choice."""
        return self.chunk.choices[0]

    @property
    def delta(self) -> ChoiceDelta:
        """Returns the delta for the 0th choice."""
        return self.choices[0].delta

    @property
    def content(self) -> Optional[str]:
        """Returns the content for the 0th choice delta."""
        return self.delta.content

    @property
    def tool_calls(self) -> Optional[list[ChoiceDeltaToolCall]]:
        """Returns the partial tool calls for the 0th choice message.

        The first `list[ChoiceDeltaToolCall]` will contain the name of the tool and
        index, and subsequent `list[ChoiceDeltaToolCall]`s will contain the arguments
        which will be strings that need to be concatenated with future
        `list[ChoiceDeltaToolCall]`s to form a complete JSON tool calls. The last
        `list[ChoiceDeltaToolCall]` will be None indicating end of stream.
        """
        return self.delta.tool_calls

    def __str__(self) -> str:
        """Returns the chunk content for the 0th choice."""
        return self.content if self.content is not None else ""


class OpenAICallParams(BaseCallParams):
    """The parameters to use when calling the OpenAI Chat API with a prompt."""

    model: str = "gpt-3.5-turbo-0125"
    base_url: Optional[str] = None
    wrapper: Optional[Callable[[OpenAI], OpenAI]] = None
    async_wrapper: Optional[Callable[[AsyncOpenAI], AsyncOpenAI]] = None
    frequency_penalty: Optional[float] = None
    logit_bias: Optional[dict[str, int]] = None
    logprobs: Optional[bool] = None
    max_tokens: Optional[int] = None
    n: Optional[int] = None
    presence_penalty: Optional[float] = None
    response_format: Optional[ResponseFormat] = None
    seed: Optional[int] = None
    stop: Union[Optional[str], list[str]] = None
    temperature: Optional[float] = None
    tool_choice: Optional[ChatCompletionToolChoiceOptionParam] = None
    tools: Optional[list[Union[Callable, Type[OpenAITool]]]] = None
    top_logprobs: Optional[int] = None
    top_p: Optional[float] = None
    user: Optional[str] = None
    # Values defined below take precedence over values defined elsewhere. Use these
    # params to pass additional parameters to the API if necessary that aren't already
    # available as params.
    extra_headers: Optional[Headers] = None
    extra_query: Optional[Query] = None
    extra_body: Optional[Body] = None
    timeout: Optional[Union[float, Timeout]] = None

    model_config = ConfigDict(arbitrary_types_allowed=True)
