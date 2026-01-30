from ollama.nemotron_client import run_nemotron

def solve(problem):
    prompt = f"""
You are a careful reasoning agent.
Solve the problem step by step.
Do not skip steps.
End with: FINAL ANSWER: <answer>

Problem:
{problem}
"""
    return run_nemotron(prompt)
