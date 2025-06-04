from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_similarity(s1: str, s2: str) -> float:
    embeddings = model.encode([s1, s2], convert_to_tensor=True)
    score = util.cos_sim(embeddings[0], embeddings[1])
    return score.item()