from ollama.nemotron_client import run_nemotron
import json

def verify(problem, reasoning, ground_truth):
    prompt = f"""
Check if the final answer matches the ground truth.

Return JSON only:
{{
  "correct": true/false
}}

Problem:
{problem}

Reasoning:
{reasoning}

Ground Truth Answer:
{ground_truth}
"""
    output = run_nemotron(prompt, temperature=0.0)
    return json.loads(output)
