import difflib

def calculate_similarity(code1, code2):
    similarity = difflib.SequenceMatcher(None, code1, code2).ratio()
    return round(similarity * 100, 2)

























