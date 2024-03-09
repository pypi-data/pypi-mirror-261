from typing import Optional
from rerankers.models import AVAILABLE_RANKERS
from rerankers.models.ranker import BaseRanker
from rerankers.utils import vprint

DEFAULTS = {
    "jina": {"en": "jina-reranker-v1-base-en"},
    "cohere": {"en": "rerank-english-v2.0", "other": "rerank-multilingual-v2.0"},
    "cross-encoder": {
        "en": "mixedbread-ai/mxbai-rerank-base-v1",
        "fr": "antoinelouis/crossencoder-camembert-base-mmarcoFR",
        "zh": "BAAI/bge-reranker-base",
        "other": "corrius/cross-encoder-mmarco-mMiniLMv2-L12-H384-v1",
    },
    "t5": {"en": "unicamp-dl/InRanker-base", "other": "unicamp-dl/mt5-base-mmarco-v2"},
    "lit5": {
        "en": "castorini/LiT5-Distill-base",
    },
    "rankgpt": {"en": "gpt-4-turbo-preview", "other": "gpt-4-turbo-preview"},
    "rankgpt3": {"en": "gpt-3.5-turbo", "other": "gpt-3.5-turbo"},
    "rankgpt4": {"en": "gpt-4", "other": "gpt-4"},
}


def _get_api_provider(model_name: str) -> str:
    PROVIDERS = ["cohere", "jina"]
    for provider in PROVIDERS:
        if provider in model_name:
            return provider


def _infer_model_type(model_name: str) -> str:
    model_name = model_name.lower()
    model_mapping = {
        "lit5": "LiT5Ranker",
        "t5": "T5Ranker",
        "inranker": "T5Ranker",
        "gpt": "RankGPTRanker",
        "zephyr": "RankZephyr",
        "cohere": "APIRanker",
        "jina": "APIRanker",
    }
    for key, value in model_mapping.items():
        if key in model_name:
            return value
    if any(keyword in model_name for keyword in ["minilm", "bert", "cross-encoders/"]):
        return "TransformerRanker"
    print(
        "Warning: Model type could not be auto-mapped. Defaulting to TransformerRanker."
    )
    print(
        "If your model is NOT intended to be ran as a one-label cross-encoder, please reload it and specify the model_type!"
    )
    return "TransformerRanker"


def _get_defaults(model_name: str, model_type: str, lang: str, verbose: int) -> str:
    if model_name == "cross-encoder":
        model_type = "TransformerRanker"
    print(f"Loading default {model_name} model for language {lang}")
    try:
        model_name = DEFAULTS[model_name][lang]
    except KeyError:
        if "other" not in DEFAULTS[model_name]:
            print(
                f"Model family {model_name} does not have a default for language {lang}"
            )
            print(
                "Aborting now... Please retry with another model family or by specifying a model"
            )
            return None, None
        model_name = DEFAULTS[model_name]["other"]
    model_type = model_type or _infer_model_type(model_name)
    vprint(f"Default Model: {model_name}", verbose)

    return model_name, model_type


def Reranker(
    model_name: str,
    lang: str = "en",
    model_type: Optional[str] = None,
    verbose: int = 1,
    **kwargs,
) -> Optional[BaseRanker]:
    model_type = _infer_model_type(model_name)
    if model_type == "APIRanker":
        kwargs["api_provider"] = _get_api_provider(model_name)
    if model_name in DEFAULTS.keys():
        model_name, model_type = _get_defaults(model_name, model_type, lang, verbose)
        if model_name is None:
            return None

    try:
        print(model_type)
        print(AVAILABLE_RANKERS)
        return AVAILABLE_RANKERS[model_type](model_name, verbose=verbose, **kwargs)
    except KeyError:
        print(
            f"You don't have the necessary dependencies installed to use {model_type}."
        )
        print(
            "Please install the necessary dependencies by running pip install rerankers[TODO]."
        )
        return None
