from abc import ABC, abstractmethod
from typing import List, Optional, Union
from rerankers.results import RankedResults


class BaseRanker(ABC):
    @abstractmethod
    def __init__(self, model_name_or_path: str, verbose: int):
        pass

    @abstractmethod
    def score(self, query: str, doc: str) -> float:
        pass

    @abstractmethod
    def rank(
        self,
        query: str,
        docs: List[str],
        doc_ids: Optional[Union[List[str], str]] = None,
    ) -> RankedResults:
        """
        End-to-end reranking of documents.
        """
        pass
