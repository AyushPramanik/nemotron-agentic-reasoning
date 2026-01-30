def curate(critique, verification):
    if not verification["correct"]:
        return False
    if critique["logical_error"]:
        return False
    if critique["confidence"] < 0.7:
        return False
    return True
