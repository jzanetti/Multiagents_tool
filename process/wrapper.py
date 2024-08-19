from typing import Literal

from process.data import read_data
from process.model import (
    create_dataframe_engine,
    load_code_model_local,
    load_embedding_model_local,
    load_llm_model_local,
    load_service,
)


def load_data_and_model(model_type: Literal["llama", "openai"] = "llama") -> dict:
    """Load data and model

    Args:
        model_type (Literal[&quot;llama&quot;, &quot;openai&quot;]): Model type in [LLAMA, OpenAI]

    Raises:
        ValueError: Invalid model type
        ValueError: Model is not implemented

    Returns:
        dict: loaded data and model
    """
    if model_type not in ["llama", "openai"]:
        raise ValueError(
            f"Invalid model_type: {model_type}. Must be 'llama' or 'openai'."
        )

    df = read_data()

    if model_type == "llama":
        embed_model = load_embedding_model_local()
        llm_code_model = load_code_model_local()
        llm_model = load_llm_model_local()
        load_service(llm_code_model, embed_model)
        query_engine = create_dataframe_engine(df)
    else:
        raise ValueError(f"{model_type} has not been implemented")

    return {"query_engine": query_engine, "data": df, "llm_model": llm_model}
