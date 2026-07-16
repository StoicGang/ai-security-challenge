from sentence_transformers import SentenceTransformer

from config import MODEL_NAME

_model = SentenceTransformer(MODEL_NAME)


def generate_embeddings(texts):
    return _model.encode(texts).tolist()


def generate_query_embedding(query):
    return _model.encode(query).tolist()