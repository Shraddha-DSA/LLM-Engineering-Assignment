import json
import subprocess
import time
import urllib.request
import psutil
import pandas as pd


MODELS = {
    "fp16": "llama3.2:3b-instruct-fp16",
    "q4": "llama3.2:3b-instruct-q4_K_M"
}

PROMPTS = [
    "What is the capital of Australia, and why isn't it Sydney?",
    "A train leaves at 14:20 and the trip takes 2h 55m. When does it arrive?",
    "If 5 machines make 5 widgets in 5 minutes, how long do 100 machines take to make 100 widgets?",
    "Write a Python function that returns the n-th Fibonacci number iteratively.",
    "Summarise in two sentences: Transformers use self-attention to weigh every token against every other token, letting them model long-range dependencies in parallel, unlike RNNs which process sequentially.",
    "Translate to French: 'The meeting has been moved to Thursday afternoon.'",
    "Write a four-line poem about monsoon rain.",
    "Explain what a hash table is to a 12-year-old.",
    "Reply with only valid JSON with keys name (string) and age (int) for a fictional person.",
    "Is it ever acceptable to lie? Give a balanced answer in under 100 words."
]

URL = "http://localhost:11434/api/generate"



def get_system_memory():

    memory = psutil.virtual_memory()

    return {
        "total_ram_gb": round(memory.total / (1024**3), 2),
        "used_ram_gb": round(memory.used / (1024**3), 2),
        "available_ram_gb": round(memory.available / (1024**3), 2),
        "ram_percent": memory.percent
    }


def get_ollama_memory():

    total = 0

    for process in psutil.process_iter(["name", "memory_info"]):

        try:
            name = (process.info["name"] or "").lower()

            if "ollama" in name:
                total += process.info["memory_info"].rss

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return round(total / (1024**3), 2)



def generate(model, prompt):

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0,
            "seed": 42,
            "num_predict": 256
        }
    }

    body = json.dumps(payload).encode()

    request = urllib.request.Request(
        URL,
        body,
        {"Content-Type": "application/json"}
    )

    with urllib.request.urlopen(request, timeout=600) as response:
        return json.load(response)


def get_ollama_status():

    try:

        with urllib.request.urlopen(
            "http://localhost:11434/api/ps",
            timeout=10
        ) as response:

            return json.load(response)

    except Exception as e:

        return {"error": str(e)}


def stop_model(model):

    payload = json.dumps({
        "model": model
    }).encode()

    request = urllib.request.Request(
        "http://localhost:11434/api/generate",
        payload,
        {"Content-Type": "application/json"},
        method="POST"
    )

    try:

        with urllib.request.urlopen(request, timeout=30):
            pass

    except Exception:
        pass

    import shutil

    ollama_path = shutil.which("ollama")

    if ollama_path:

        subprocess.run(
            [ollama_path, "stop", model],
            capture_output=True,
            text=True
        )



try:

    urllib.request.urlopen(
        "http://localhost:11434",
        timeout=5
    )

except Exception:

    print("ERROR: Ollama is not running.")
    print("Start Ollama and try again.")

    raise SystemExit(1)



results = {}

for label, model in MODELS.items():

    print(f"\n========== {label.upper()} ==========")

    print("Loading model and performing warm-up...")

    generate(model, "Hello")

    runs = []

    peak_ram = 0
    peak_ollama_ram = 0

    for i, prompt in enumerate(PROMPTS, 1):

        before = get_system_memory()

        start = time.perf_counter()

        data = generate(model, prompt)

        end = time.perf_counter()

        eval_count = data.get("eval_count", 0)

        eval_duration = data.get("eval_duration", 0) / 1e9

        tps = (
            eval_count / eval_duration
            if eval_duration > 0 else 0
        )

        after = get_system_memory()

        ollama_ram = get_ollama_memory()

        peak_ram = max(
            peak_ram,
            after["used_ram_gb"]
        )

        peak_ollama_ram = max(
            peak_ollama_ram,
            ollama_ram
        )

        run = {

            "prompt": prompt,

            "output": data.get("response", ""),

            "output_tokens": eval_count,

            "tokens_per_second": round(tps, 2),

            "generation_time_sec": round(eval_duration, 3),

            "total_time_sec": round(end - start, 3),

            "ram_before_gb": before["used_ram_gb"],

            "ram_after_gb": after["used_ram_gb"],

            "ollama_ram_gb": ollama_ram

        }

        runs.append(run)

        print(
            f"Prompt {i}/10 | "
            f"{tps:.2f} tokens/sec | "
            f"RAM: {after['used_ram_gb']} GB"
        )

    ollama_status = get_ollama_status()

    results[label] = {

        "model": model,

        "average_tokens_per_second": round(
            sum(r["tokens_per_second"] for r in runs) / len(runs),
            2
        ),

        "peak_system_ram_gb": peak_ram,

        "peak_ollama_ram_gb": peak_ollama_ram,

        "final_memory": get_system_memory(),

        "ollama_ps": ollama_status,

        "runs": runs

    }

    print("\nAverage speed:",
          results[label]["average_tokens_per_second"],
          "tokens/sec")

    print("Peak system RAM:",
          peak_ram, "GB")

    print("Peak Ollama RAM:",
          peak_ollama_ram, "GB")

    print("\nUnloading model...")

    stop_model(model)

    time.sleep(3)



with open("results.json", "w", encoding="utf-8") as file:

    json.dump(results, file, indent=4)


summary = []

for label, result in results.items():

    summary.append({

        "Configuration": label,

        "Model": result["model"],

        "Average Tokens/sec":
            result["average_tokens_per_second"],

        "Peak System RAM (GB)":
            result["peak_system_ram_gb"],

        "Peak Ollama RAM (GB)":
            result["peak_ollama_ram_gb"],

        "Model Size (GB)":
            6.4 if label == "fp16" else 2.0

    })


df = pd.DataFrame(summary)

df.to_csv("summary.csv", index=False)



with open("results.md", "w", encoding="utf-8") as file:

    file.write("# LLM Quantisation Benchmark\n\n")

    file.write("Comparison: FP16 vs Q4_K_M\n\n")

    for i, prompt in enumerate(PROMPTS):

        file.write(f"\n## Prompt {i+1}\n\n")

        file.write(f"**Question:** {prompt}\n\n")

        for label in MODELS:

            response = results[label]["runs"][i]

            file.write(f"### {label.upper()}\n\n")

            file.write(
                f"Speed: {response['tokens_per_second']} tokens/sec\n\n"
            )

            file.write(response["output"] + "\n\n")

        file.write(
            "**Quality Score (0-5):** "
            "FP16: ___ | Q4: ___\n\n"
        )

        file.write("**Observations:** ___\n\n")

        file.write("---\n")


print("\n===================================")

print("BENCHMARK COMPLETED SUCCESSFULLY")

print("===================================")

print(df.to_string(index=False))

print("\nGenerated files:")

print("1. results.json")
print("2. results.md")
print("3. summary.csv")