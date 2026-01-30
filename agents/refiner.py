from ollama.nemotron_client import run_nemotron

def refine(problem, reasoning, critique):
    prompt = f"""
Improve the reasoning below.
Fix logical errors and missing steps.
Preserve the final answer.

Problem:
{problem}

Critique:
{critique}

Original Reasoning:
{reasoning}
"""
    return run_nemotron(prompt, temperature=0.5)
