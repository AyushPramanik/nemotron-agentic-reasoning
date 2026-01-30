def token_efficiency(reasoning, correct):
    tokens = len(reasoning.split())
    return tokens if correct else None
