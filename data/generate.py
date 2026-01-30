from pipelines.agentic_loop import run_pipeline
import json

with open("data/raw/gsm8k.json") as f:
    dataset = json.load(f)

curated = []

for item in dataset:
    result = run_pipeline(item["question"], item["answer"])
    if result["keep"]:
        curated.append(result)

with open("data/curated/gsm8k_curated.json", "w") as f:
    json.dump(curated, f, indent=2)
