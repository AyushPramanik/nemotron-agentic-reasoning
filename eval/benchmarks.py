def accuracy(results):
    return sum(r["keep"] for r in results) / len(results)
