import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def run_nemotron(
    prompt,
    model="nemotron:8b-q4",
    temperature=0.7,
    max_tokens=400
):
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": temperature,
            "num_predict": max_tokens
        }
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    return response.json()["response"]
