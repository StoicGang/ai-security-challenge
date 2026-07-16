from config import (
    DEFAULT_CHUNK_SIZE,
    DEFAULT_OVERLAP
)

def read_document(document_path):
    with open(document_path, "r", encoding="utf-8") as file:
        return file.read()

def chunk_document(
    document,
    chunk_size=DEFAULT_CHUNK_SIZE,
    overlap=DEFAULT_OVERLAP
):
    step_size = chunk_size - overlap
    chunks = []

    for i in range(0, len(document), step_size):
        chunk = document[i:i + chunk_size]
        chunks.append(chunk)

    return chunks