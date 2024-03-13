from typing import Any, Optional, Sequence

from langchain.retrievers.document_compressors.base import BaseDocumentCompressor
from langchain_core.callbacks.manager import Callbacks
from langchain_core.documents import Document


class RerankerLangChainCompressor(BaseDocumentCompressor):
    model: Any
    kwargs: dict = {}
    k: int = 5

    class Config:
        """Configuration for this pydantic object."""

        arbitrary_types_allowed = True

    def compress_documents(
        self,
        documents: Sequence[Document],
        query: str,
        callbacks: Optional[Callbacks] = None,  # noqa
        **kwargs,
    ) -> Any:
        """Rerank a list of documents relevant to a query."""
        doc_list = list(documents)
        _docs = [d.page_content for d in doc_list]
        results = self.model.rank(
            query=query,
            documents=_docs,
            k=kwargs.get("k", self.k),
            **self.kwargs,
        )
        final_results = []
        for r in results.top_k(self.k):
            doc = doc_list[r["rank"]]
            doc.metadata["relevance_score"] = r["score"]
            final_results.append(doc)
        return final_results
