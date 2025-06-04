import argparse
from matcher.traditional import levenshtein_similarity
from matcher.fuzzy import fuzzy_ratio
from matcher.semantic import semantic_similarity

def main():
    parser = argparse.ArgumentParser(description="Compare two strings using various similarity methods.")
    parser.add_argument("s1", help="First string")
    parser.add_argument("s2", help="Second string")
    args = parser.parse_args()

    print(f"Levenshtein similarity: {levenshtein_similarity(args.s1, args.s2):.2f}")
    print(f"Fuzzy match ratio: {fuzzy_ratio(args.s1, args.s2):.2f}")
    print(f"Semantic similarity: {semantic_similarity(args.s1, args.s2):.2f}")

if __name__ == "__main__":
    main()