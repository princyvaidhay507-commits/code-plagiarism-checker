from difflib import SequenceMatcher

def calculate_similarity(code1, code2):
    return SequenceMatcher(None, code1, code2).ratio() * 100