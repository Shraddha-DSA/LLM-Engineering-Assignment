# LLM Engineering Assignment

A practical implementation of three core LLM engineering concepts: Fine-Tuning, Retrieval-Augmented Generation (RAG), and Local LLM Inference Optimization.

## Tasks Overview

### Task 1: Fine-Tuning with LoRA

Fine-tuned Qwen2.5-0.5B-Instruct using Low-Rank Adaptation (LoRA) for converting customer support messages into structured JSON outputs.

**Key Highlights:**
- Parameter-efficient fine-tuning using LoRA.
- Synthetic dataset generation.
- Base vs fine-tuned model evaluation.
- In-distribution and out-of-distribution testing.
- Failure analysis and GPU memory estimation.

**Results:**
- ID Exact Match: 100%
- OOD Exact Match: 58.7%

### Task 2: RAG from Scratch

Built a document-based question-answering system using the 48-page NIST AI Risk Management Framework.

**Key Highlights:**
- PDF extraction and preprocessing.
- Text chunking with overlap.
- Semantic embeddings using BGE-small.
- Dense retrieval using NumPy.
- BM25 keyword retrieval.
- Hybrid retrieval using Reciprocal Rank Fusion.
- Cross-encoder re-ranking.
- Evaluation using 15 manually created questions.

**Best Result:** Recall@5 of 80%.

### Task 3: Local LLM Inference & Optimization

Benchmarked a small open-weight language model under different precision and quantization settings.

**Key Highlights:**
- FP16 vs quantized inference.
- Tokens-per-second benchmarking.
- Memory consumption analysis.
- Output quality comparison.
- KV cache and quantization analysis.
- Concurrent serving strategy for 20 users on a 24 GB GPU.

## Technology Stack

| Category | Technologies |
|---|---|
| Language | Python |
| Deep Learning | PyTorch |
| Fine-Tuning | Transformers, PEFT, LoRA |
| Embeddings | Sentence Transformers, BGE |
| Retrieval | NumPy, BM25, FAISS |
| Re-ranking | Cross-Encoder |
| Data Processing | Pandas, NumPy |
| Environment | Google Colab, VS Code |

## Repository Structure

```text
LLM-Engineering-Assignment/
│
├── Task_1_Fine_Tuning/
├── Task_2_RAG/
├── Task_3_Local_Inference/
├── Report.pdf
└── README.md
```

## How to Run

1. Clone this repository.
2. Install the dependencies required for the respective task.
3. Open the corresponding notebook or Python script.
4. Follow the execution instructions provided in each task folder.

## Author

**Shraddha Tiwari**

AI/ML Engineer | Backend Developer | Open Source Contributor

GitHub: https://github.com/Shraddha-DSA