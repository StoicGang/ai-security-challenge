from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "I enjoy learning artificial intelligence.",
    "I like studying AI and Cybersecurity.",
    "I love solving tryhackme CTFs",
    "The weather is pleasant today.",
    "My favorite food is pizza.",
    "Penguins live in Antarctica."
]


embeddings = model.encode(sentences)

similar = cosine_similarity(
    [embeddings[0]],
    [embeddings[1]]
)[0][0]

unrelated = cosine_similarity(
    [embeddings[0]],
    [embeddings[4]]
)[0][0]

print(f"Sentence 1 ↔ Sentence 2: {similar:.4f}")
print(f"Sentence 1 ↔ Sentence 5: {unrelated:.4f}")