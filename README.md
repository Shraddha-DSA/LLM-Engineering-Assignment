# Task 3 – Running a Model Locally & Optimisation

## 1. Overview

This task focuses on running an open-weight Large Language Model locally using **Ollama** and comparing two model configurations:

- FP16 (Full Precision)
- Q4_K_M (4-bit Quantization)

The objective is to understand how quantization impacts model size, inference speed, memory consumption, and response quality.

---

## 2. Hardware & Environment

| Component | Specification |
|---|---|
| Processor | Intel Core i5-1235U (12th Gen) |
| RAM | 16 GB |
| GPU | Intel UHD Graphics |
| NVIDIA GPU | Not Available |
| Operating System | Windows |
| Runtime | Ollama |
| Model | Llama 3.2 3B Instruct |

**Note:** Both models were evaluated using CPU-based inference. No NVIDIA GPU acceleration was available.

---

## 3. Models Used

Two configurations of Llama 3.2 3B Instruct were downloaded using Ollama.

| Model | Precision | Approx. Disk Size |
|---|---|---:|
| Llama 3.2 3B Instruct | FP16 | 6.4 GB |
| Llama 3.2 3B Instruct | Q4_K_M | 2.0 GB |

### Download Models

```bash
ollama pull llama3.2:3b-instruct-fp16
ollama pull llama3.2:3b-instruct-q4_K_M
```

### Verify Installed Models

```bash
ollama list
```

---

## 4. Benchmark Methodology

Both models were evaluated using the same set of 10 prompts to ensure a fair comparison.

The prompts covered:

1. Factual Question Answering
2. Time Calculation
3. Logical Reasoning
4. Python Code Generation
5. Technical Explanation
6. Translation
7. Creative Writing
8. Concept Explanation
9. Structured JSON Generation
10. Ethical Reasoning

### Benchmark Configuration

| Parameter | Value |
|---|---|
| Temperature | 0 |
| Seed | 42 |
| Maximum Output Tokens | 256 |
| Number of Prompts | 10 |
| API | Ollama Generate API |

### Metrics Collected

- Tokens per second
- Peak system RAM
- Model disk size
- Response quality

---

## 5. Benchmark Results

### Performance Comparison

| Metric | FP16 | Q4_K_M |
|---|---:|---:|
| Average Tokens/sec | 2.56 | 6.96 |
| Model Disk Size | 6.4 GB | 2.0 GB |
| Peak System RAM | 14.15 GB | 13.83 GB |

### Key Observations

**Inference Speed**

Q4_K_M achieved an average generation speed of 6.96 tokens/sec compared to 2.56 tokens/sec for FP16.

This represents approximately **2.72× faster generation**.

**Model Size**

The quantized model required approximately 2.0 GB of disk space compared to 6.4 GB for FP16.

This represents approximately **68.75% reduction in model storage size**.

**Memory Usage**

The observed peak system RAM was:

- FP16: 14.15 GB
- Q4_K_M: 13.83 GB

These measurements represent system-wide memory usage, not isolated model memory consumption.

---

## 6. Response Quality Evaluation

Both models were evaluated using identical prompts.

| Task | FP16 | Q4_K_M |
|---|---|---|
| Factual Question Answering | Correct | Correct |
| Time Calculation | Correct | Correct |
| Logical Reasoning | Correct | Correct |
| Python Code Generation | Correct | Edge-case issue |
| Technical Explanation | Good | Good |
| Translation | Good | Good |
| Creative Writing | Good | Good |
| Concept Explanation | More complete | Truncated |
| JSON Generation | Valid JSON | Valid JSON |
| Ethical Reasoning | Good | Good |

### Important Observations

- Both models performed similarly on most tasks.
- FP16 handled the Fibonacci edge case `n = 1` correctly.
- Q4_K_M missed the `n = 1` edge case in its generated implementation.
- Both models generated valid JSON.
- Q4_K_M produced a more noticeably truncated response in the concept explanation.

**Conclusion:** Quantization provided significant performance and storage benefits, with some differences in response quality on specific tasks.

---

## 7. Understanding Quantization

Quantization reduces the numerical precision used to represent model weights.

For example:

- FP16 represents weights using 16-bit floating-point values.
- Q4_K_M uses a 4-bit quantized representation with additional quantization metadata.

### Benefits

1. Reduces model storage requirements.
2. Lowers memory requirements for model weights.
3. Can improve inference speed.
4. Makes it possible to run larger models on resource-constrained systems.

### Trade-offs

1. Can introduce numerical approximation errors.
2. May slightly reduce response quality.
3. Can affect coding accuracy and reasoning in certain cases.

In this experiment, Q4_K_M achieved significantly better inference speed while maintaining broadly comparable response quality.

---

## 8. Understanding KV Cache

KV Cache stands for **Key-Value Cache**.

During autoregressive text generation, a Transformer processes tokens sequentially. For each token, it calculates Key and Value representations in its attention layers.

Instead of recalculating these representations for all previous tokens every time a new token is generated, the model stores them in memory.

### Benefits

- Avoids repeated computation.
- Improves generation efficiency.
- Reduces inference latency.

### Trade-offs

- Consumes RAM or VRAM.
- Memory usage increases with context length.
- Larger models and higher concurrency increase cache requirements.

KV Cache is particularly important when serving multiple users simultaneously.

---

## 9. Serving 20 Concurrent Users on a 24 GB GPU

For serving approximately 20 concurrent users, the following architecture can be considered.

### Proposed Architecture

- **Model:** 7B parameter model with 4-bit quantization.
- **Inference Engine:** vLLM.
- **API Layer:** FastAPI.
- **Batching:** Continuous batching.
- **Memory Management:** PagedAttention.
- **Concurrency Management:** Request queue and controlled batching.

### Illustrative GPU Memory Budget

| Component | Estimated Memory |
|---|---:|
| Quantized Model Weights | 4–5 GB |
| KV Cache | 4–6 GB |
| CUDA and Runtime Overhead | ~2 GB |
| Activations and Temporary Buffers | ~3 GB |
| Available Headroom | Remaining memory |
| **Total GPU Capacity** | **24 GB** |

These are planning estimates, not guaranteed memory requirements. Actual KV Cache consumption depends on model architecture, context length, batch size, and cache precision.

### Optimisation Strategies

1. Use quantized model weights to reduce memory consumption.
2. Apply continuous batching to process multiple requests efficiently.
3. Use PagedAttention for efficient KV Cache management.
4. Set reasonable context-length and output-token limits.
5. Implement request queuing and backpressure.
6. Monitor GPU utilisation, memory usage, and inference latency.
7. Perform load testing to determine sustainable concurrency.

**Note:** Supporting 20 concurrent users does not necessarily mean generating 20 responses simultaneously at maximum speed. Actual throughput depends on the model, GPU, context length, and request workload.

---

## 10. Final Conclusion

This experiment demonstrated the practical benefits of running quantized LLMs locally.

The comparison between Llama 3.2 3B FP16 and Q4_K_M showed that:

- Q4_K_M was approximately 2.72× faster.
- Model storage requirements decreased by approximately 68.75%.
- Response quality remained broadly comparable across most tested prompts.
- Some differences appeared in code generation and response completeness.

Considering the hardware limitations of the test system, **Q4_K_M was the more practical choice for local inference**.

The experiment also provided practical insights into quantization, KV Cache management, inference optimisation, and serving multiple concurrent users.

---

## 11. Technologies Used

- Python
- Ollama
- Llama 3.2 3B Instruct
- FP16
- Q4_K_M Quantization
- REST API
- Performance Benchmarking

---

## 12. Project Structure

```text
Task_3_Local_Inference/
│
├── benchmark.py
├── results.json
├── results.md
├── summary.csv
└── README.md
```
