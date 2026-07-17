from sentence_transformers import SentenceTransformer

from config import EMBEDDING_MODEL_NAME

# SentenceTransformer expects a huggingface model id like "all-MiniLM-L6-v2"
_model = SentenceTransformer(EMBEDDING_MODEL_NAME)


def generate_embeddings(texts):
    return _model.encode(texts).tolist()


def generate_query_embedding(query):
    return _model.encode(query).tolist()