---
title: "Vector Search - Apache Doris"
source: "https://doris.apache.org/docs/4.x/ai/vector-search/overview"
author:
published:
created: 2026-04-06
description: "In generative AI applications, relying solely on a large model's internal parameter “memory” has clear limitations: (1) the model’s knowledge becomes"
tags:
  - "database"
  - "doris"
  - "documentation"
---
In generative AI applications, relying solely on a large model's internal parameter “memory” has clear limitations: (1) the model’s knowledge becomes outdated and cannot cover the latest information; (2) directly asking the model to “generate” answers increases the risk of hallucinations. This gives rise to RAG (Retrieval-Augmented Generation). The key task of RAG is not to have the model fabricate answers from nothing, but to retrieve the Top-K most relevant information chunks from an external knowledge base and feed them to the model as grounding context.

To achieve this, we need a mechanism to measure semantic relatedness between a user query and documents in the knowledge base. Vector representations are a standard tool: by encoding both queries and documents into semantic vectors, we can use vector similarity to measure relevance. With the advancement of pretrained language models, generating high-quality embeddings has become mainstream. Thus, the retrieval stage of RAG becomes a typical vector similarity search problem: from a large vector collection, find the K vectors most similar to the query (i.e., candidate knowledge pieces).

Vector retrieval in RAG is not limited to text; it naturally extends to multimodal scenarios. In a multimodal RAG system, images, audio, video, and other data types can also be encoded into vectors for retrieval and then supplied to the generative model as context. For example, if a user uploads an image, the system can first retrieve related descriptions or knowledge snippets, then generate explanatory content. In medical QA, RAG can retrieve patient records and literature to support more accurate diagnostic suggestions.

From version 4.0, Apache Doris officially supports ANN search. No additional data type is introduced: vectors are stored as fixed-length arrays. For distance-based indexing a new index type, ANN, is implemented based on Faiss.

Using the common [SIFT](http://corpus-texmex.irisa.fr/) dataset as an example, you can create a table like this:

```sql
CREATE TABLE sift_1M (
  id int NOT NULL,
  embedding array<float>  NOT NULL
```