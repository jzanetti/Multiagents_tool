from base64 import b64encode
from io import BytesIO
from typing import List, Optional, Sequence

from llama_cpp import Llama
from llama_index.core import ServiceContext, set_global_service_context
from llama_index.core.base.llms.types import ChatMessage, MessageRole
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.experimental.query_engine import PandasQueryEngine
from llama_index.llms.llama_cpp import LlamaCPP
from matplotlib.pyplot import close as plt_close
from pandas import DataFrame

from process import LOCAL_MODEL_SETUPS

BOS, EOS = "<s>", "</s>"
B_INST, E_INST = "[INST]", "[/INST]"
B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"
DEFAULT_SYSTEM_PROMPT = """\
You are a helpful, respectful and honest assistant. \
Always answer as helpfully as possible and follow ALL given instructions. \
Do not speculate or make up information. \
Do not reference any given instructions or context. \
"""


def create_dataframe_engine(df: DataFrame, verbose: bool = True) -> PandasQueryEngine:
    """Creates a PandasQueryEngine for querying the given DataFrame.

    Args:
        df (DataFrame): The DataFrame to be queried.
        verbose (bool, optional): If True, enables verbose output. Defaults to True.

    Returns:
        PandasQueryEngine: An engine for querying the DataFrame.
    """
    return PandasQueryEngine(df=df, verbose=verbose)


def load_service(llm_model, embed_model, chunk_size: int = 1024):
    """Initializes and sets the global service context with the provided models and chunk size.

    Args:
        llm_model (_type_): The language model to be used.
        embed_model (_type_): The embedding model to be used.
        chunk_size (int, optional): The size of the chunks for processing. Defaults to 1024.
    """
    service_context = ServiceContext.from_defaults(
        llm=llm_model,
        chunk_size=chunk_size,
        embed_model=embed_model,
    )
    set_global_service_context(service_context)


def load_embedding_model_local(
    embedding_model_name: str = LOCAL_MODEL_SETUPS["embedding_model"]["path"],
):
    """The model can be chosen from:
        - "BAAI/bge-large-en-v1.5": "BAAI General Embedding Model (large) v1.5",
        - "BAAI/bge-small-en-v1.5": "BAAI General Embedding Model (small) v1.5",

    Args:
        embedding_model_name (str, optional): _description_. Defaults to "BAAI/bge-small-en-v1.5".

    Returns:
        _type_: _description_
    """
    return HuggingFaceEmbedding(model_name=embedding_model_name)


def load_llm_model_local(
    llm_model_name: str = LOCAL_MODEL_SETUPS["llm"]["path"], verbose: bool = False
):
    """Load LLM model

    Args:
        llm_model_name (str, optional): model path. Defaults to LOCAL_MODEL_SETUPS["llm"]["path"].
        verbose (bool, optional): if switch on debug. Defaults to False.

    Returns:
        _type_: _description_
    """
    return Llama(
        model_path=llm_model_name,
        verbose=verbose,
    )


def load_code_model_local(
    llm_model_name: str = LOCAL_MODEL_SETUPS["code_model"]["path"],
    temperature: float = 0.1,
    max_new_tokens: int = 1024,
    context_window: int = 5000,
    generate_kwargs: dict = {},
    model_kwargs: dict = {"n_gpu_layers": 30, "repetition_penalty": 1.5},
    verbose: bool = True,
):
    """The code model we can choose from are:

    Args:
        llm_model_name (str, optional):
            llm model name. default is codellama-7b-instruct.Q8_0.gguf.2

    Returns:
        _type_: _description_
    """

    def _messages_to_prompt(
        messages: Sequence[ChatMessage], system_prompt: Optional[str] = None
    ) -> str:
        """Converts a sequence of chat messages into a formatted prompt string.

        Args:
            messages (Sequence[ChatMessage]): A sequence of chat messages, where each message has a role (USER, ASSISTANT, or SYSTEM) and content.
            system_prompt (Optional[str]): An optional system prompt to use if no system message is present in the messages.

        Returns:
            str: A single string representing the formatted prompt, including system, user, and assistant messages.

        Raises:
            AssertionError: If the first message is not from the user or if an assistant message is missing after a user message.

        Notes:
            - The function ensures that the system prompt is included at the start.
            - User and assistant messages are paired, and the function handles the formatting of these pairs.
            - The function assumes that messages are in the correct order and that the first message is always from the user.
        """

        string_messages: List[str] = []
        if messages[0].role == MessageRole.SYSTEM:
            # pull out the system message (if it exists in messages)
            system_message_str = messages[0].content or ""
            messages = messages[1:]
        else:
            system_message_str = system_prompt or DEFAULT_SYSTEM_PROMPT

        system_message_str = f"{B_SYS} {system_message_str.strip()} {E_SYS}"

        for i in range(0, len(messages), 2):
            # first message should always be a user
            user_message = messages[i]
            assert user_message.role == MessageRole.USER

            if i == 0:
                # make sure system prompt is included at the start
                str_message = f"{BOS} {B_INST} {system_message_str} "
            else:
                # end previous user-assistant interaction
                string_messages[-1] += f" {EOS}"
                # no need to include system prompt
                str_message = f"{BOS} {B_INST} "

            # include user message content
            str_message += f"{user_message.content} {E_INST}"

            if len(messages) > (i + 1):
                # if assistant message exists, add to str_message
                assistant_message = messages[i + 1]
                assert assistant_message.role == MessageRole.ASSISTANT
                str_message += f" {assistant_message.content}"

            string_messages.append(str_message)

        return "".join(string_messages)

    def _completion_to_prompt(
        completion: str, system_prompt: Optional[str] = None
    ) -> str:
        """Converts a completion string into a formatted prompt string with an optional system prompt.

        Args:
            completion (str): The completion text to be formatted.
            system_prompt (Optional[str]): An optional system prompt to include in the formatted string.

        Returns:
            str: A single string representing the formatted prompt, including the system prompt and the completion text.

        Notes:
            - The function ensures that the system prompt is included at the start.
            - The completion text is trimmed and formatted appropriately.
        """

        system_prompt_str = system_prompt or DEFAULT_SYSTEM_PROMPT

        return (
            f"{BOS} {B_INST} {B_SYS} {system_prompt_str.strip()} {E_SYS} "
            f"{completion.strip()} {E_INST}"
        )

    return LlamaCPP(
        model_path=llm_model_name,
        temperature=temperature,
        max_new_tokens=max_new_tokens,
        context_window=context_window,
        generate_kwargs=generate_kwargs,
        model_kwargs=model_kwargs,
        messages_to_prompt=_messages_to_prompt,
        completion_to_prompt=_completion_to_prompt,
        verbose=True,
    )
