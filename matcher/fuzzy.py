from fuzzywuzzy import fuzz

def fuzzy_ratio(s1: str, s2: str) -> float:
    return fuzz.ratio(s1, s2) / 100.0