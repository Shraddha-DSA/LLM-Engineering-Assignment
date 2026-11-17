# Task 1: Fine-Tuning with LoRA

## Overview

Fine-tuned Qwen2.5-0.5B-Instruct using Low-Rank Adaptation (LoRA) to convert customer support messages into structured JSON outputs.

## Model & Configuration

- **Base Model:** Qwen2.5-0.5B-Instruct
- **Technique:** LoRA
- **Frameworks:** PyTorch, Transformers, PEFT
- **Dataset:** Synthetic customer support dataset

## LoRA Hyperparameters

| Parameter | Value |
|---|---|
| Rank | 16 |
| Alpha | 32 |
| Dropout | 0.05 |
| Learning Rate | 2e-4 |
| Epochs | 3 |
| Batch Size | 8 |

## Dataset Distribution

| Split | Examples |
|---|---:|
| Training | 1200 |
| Validation | 150 |
| Test ID | 150 |
| Test OOD | 150 |

## Evaluation Results

| Model | ID Exact Match | OOD Exact Match |
|---|---:|---:|
| Base Zero-shot | 2.7% | 2.7% |
| Base 5-shot | 15.3% | 12.7% |
| Fine-tuned LoRA | 100% | 58.7% |

## Deliverables

- Fine-tuning notebook
- Saved LoRA adapter
- Evaluation predictions
- Comparison metrics
- Failure analysis
- 7B GPU memory estimation

## Execution

Open `Task1_LoRA_Fine_Tuning.ipynb` in Google Colab with GPU runtime enabled.