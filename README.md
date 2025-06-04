# AI String Matcher

This project compares string similarity using traditional, fuzzy, and semantic AI methods.

## Features
- Levenshtein Distance
- Fuzzy Matching (FuzzyWuzzy)
- Semantic Similarity (Sentence Transformers)
- Real-world test with Quora duplicate questions

## Setup
```bash
pip install -r requirements.txt
```

## CLI Usage
```bash
python cli.py "How do I learn Python?" "What is the best way to learn Python?"
```

## Dataset Notebook
Explore `notebooks/quora_analysis.ipynb` to evaluate model performance on real data.