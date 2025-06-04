import Levenshtein

def levenshtein_similarity(s1: str, s2: str) -> float:
    distance = Levenshtein.distance(s1, s2)
    max_len = max(len(s1), len(s2))
    return 1 - distance / max_len if max_len > 0 else 1.0