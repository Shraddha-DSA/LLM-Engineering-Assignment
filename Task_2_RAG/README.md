# Task 2: Retrieval-Augmented Generation (RAG) from Scratch

## Overview

Built a document-based question-answering system using the 48-page NIST AI Risk Management Framework.

The implementation uses embedding-based retrieval, BM25, hybrid search, and cross-encoder re-ranking without LangChain or LlamaIndex.

## Technology Stack

- Python
- PyMuPDF
- Sentence Transformers
- BGE-small-en-v1.5
- NumPy
- BM25
- Cross-Encoder

## Implementation

1. PDF extraction and text preprocessing.
2. Text chunking with 120-word and 250-word configurations.
3. Semantic embedding generation.
4. Dense vector retrieval using NumPy.
5. Keyword-based retrieval using BM25.
6. Hybrid retrieval using Reciprocal Rank Fusion.
7. Cross-encoder re-ranking.

## Retrieval Evaluation

15 manually created questions with corresponding source passages were used for evaluation.

| Method | Chunk Size | Recall@5 |
|---|---:|---:|
| Dense | 120 | 66.7% |
| Dense | 250 | 66.7% |
| BM25 | 120 | 33.3% |
| BM25 | 250 | 33.3% |
| Hybrid + Re-ranking | 120 | 80% |
| Hybrid + Re-ranking | 250 | 80% |

## Deliverables

- RAG implementation notebook
- Gold questions and source passages
- Retrieval evaluation results
- Failure analysis

## Execution

Open `Task_2_RAG_From_Scratch.ipynb` in Google Colab and execute the notebook cells sequentially.