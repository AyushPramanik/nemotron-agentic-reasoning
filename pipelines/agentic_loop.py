from agents.solver import solve
from agents.critic import critique
from agents.verifier import verify
from agents.refiner import refine
from agents.curator import curate

def run_pipeline(problem, answer):
    reasoning = solve(problem)
    critique_result = critique(problem, reasoning)
    verification = verify(problem, reasoning, answer)

    if critique_result["logical_error"]:
        reasoning = refine(problem, reasoning, critique_result)
        critique_result = critique(problem, reasoning)
        verification = verify(problem, reasoning, answer)

    keep = curate(critique_result, verification)

    return {
        "problem": problem,
        "reasoning": reasoning,
        "keep": keep
    }
