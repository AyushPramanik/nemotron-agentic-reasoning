from ollama.nemotron_client import run_nemotron
import json

def critique(problem, reasoning):
    prompt = f"""
You are a logic critic.
Analyze the reasoning below.

Return JSON only:
{{
  "logical_error": true/false,
  "missing_steps": true/false,
  "confidence": 0.0-1.0
}}

Problem:
{problem}

Reasoning:
{reasoning}
"""
    output = run_nemotron(prompt, temperature=0.2)
    return json.loads(output)
