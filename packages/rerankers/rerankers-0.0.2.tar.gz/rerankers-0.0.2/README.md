
## TL;DR

**UNDER CONSTRUCTION**


Load any reranker, no matter the architecture:
```python
from rerankers import Reranker

# Cross-encoder default
ranker = Reranker('cross-encoder')

# Specific cross-encoder
ranker = Reranker('mixedbread-ai/mxbai-rerank-xlarge-v1')

# T5 Seq2Seq reranker
ranker = Reranker("t5")

# Specific T5 Seq2Seq reranker
ranker = Reranker("unicamp-dl/InRanker-base")

# API (Cohere)
ranker = Reranker("cohere", lang='en' (or 'other'), api_key = API_KEY)

# API (Jina)
ranker = Reranker("jina", api_key = API_KEY)

# RankGPT4-turbo
ranker = Reranker("rankgpt", api_key = API_KEY)

# RankGPT3-turbo
ranker = Reranker("rankgpt3", api_key = API_KEY)

```

Then:

```python
results = ranker.rank(query="I love you", docs=["I hate you", "I really like you", "I like you", "I despise you"])
```

You can also pass a list of `doc_ids` to `rank()`. If you don't, it'll be auto-generated and each doc_id will correspond to the index of any given document in `docs`.

Which will always return a `RankedResults` pydantic object, containing a list of `Result`s:

```python
RankedResults(results=[Result(doc_id=2, text='I like you', score=0.13376183807849884, rank=1), Result(doc_id=1, text='I really like you', score=0.002901385771110654, rank=2), Result(doc_id=0, text='I hate you', score=-2.278848886489868, rank=3), Result(doc_id=3, text='I despise you', score=-3.1964476108551025, rank=4)], query='I love you', has_scores=True)
```

You can retrieve however many top results by running .top_k() on a `RankedResults` object:

```python
> results.top_k(1)
[Result(doc_id=2, text='I like you', score=0.13376183807849884, rank=1)]
> results.top_k(1)[0]['text']
'I like you'
```

You can also retrieve the score for a given doc_id. This is useful if you're scoring documents to use for knowledge distillation:

```python
> results.get_score_by_docid(3)
-2.278848886489868
```

For the same purpose, you can also use `ranker.score()` to score a single Query-Document pair:
```python
> ranker.score(query="I love you", doc="I hate you")
-2.278848886489868
```

Please note, `score` is not available for RankGPT rerankers, as they don't issue individual relevance scores but a list of ranked results!
## Features

Legend:
- ✅ Supported
- 🟠 Implemented, but not fully fledged
- 📍Not supported but intended to be in the future
- ❌ Not supported & not currently planned

Supported models:
- ✅ Any standard SentenceTransformer or Transformers cross-encoder
- 🟠 RankGPT (Implemented using original repo, but missing the rankllm's repo improvements)
- ✅ T5-based pointwise rankers (InRanker, MonoT5...)
- ✅ Cohere API rerankers
- ✅ Jina API rerankers
- 🟠 ColBERT-based reranker - not a model initially designed for reranking, but quite strong (Implementation could be optimised and is from a third party implementation.)
- 📍 MixedBread API (Reranking API not yet released)
- 📍 RankLLM/RankZephyr (Proper RankLLM implementation should replace the unsafe RankGPT one)
- 📍 LiT5

Supported features:
- ✅ Reranking 
- 📍 Training on Python >=3.10 (via interfacing with other libraries)
- 📍 ONNX runtime support (quantised rankers, more efficient inference, etc...)
- ❌(📍Maybe?) Training via rerankers directly
## Usage
  
