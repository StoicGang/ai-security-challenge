from common.chunking import read_document, chunk_document
from common.embedding import generate_embeddings, generate_query_embedding
from common.vector_db import (
    create_collection,
    store_embeddings,
    query_collection,
)

def retrieve_context(
    document_path: str,
    query: str,
    n_results: int = 4,
) -> dict:
    # 1. Read and chunk the document
    document = read_document(document_path)
    chunks = chunk_document(document)

    # 2. Generate embeddings for chunks
    embeddings = generate_embeddings(chunks)
    ids = [f"chunk_{index}" for index in range(len(chunks))]

    # 3. Store in vector database
    collection = create_collection()
    store_embeddings(
        collection=collection,
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
    )

    # 4. Embed query and search collection
    query_embedding = generate_query_embedding(query)
    results = query_collection(
        collection=collection,
        query_embedding=query_embedding,
        n_results=n_results,
    )

    # 5. Extract and format the context strings
    retrieved_chunks = results["documents"][0]
    context = "\n\n".join(retrieved_chunks)

    return {
        "query": query,
        "retrieved_chunks": retrieved_chunks,
        "context": context
    }