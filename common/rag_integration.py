from common.chunking import read_document, chunk_document
from common.embedding import generate_embeddings, generate_query_embedding
from common.vector_db import (
    create_collection,
    store_embeddings,
    query_collection,
)
from common.prompts import RAG_PROMPT
from common.gemini_client import generate_content



def run_rag(
    document_path,
    query,
    n_results=4,
    prompt_template=RAG_PROMPT,
):
    # Read and chunk the document
    document = read_document(document_path)
    chunks = chunk_document(document)

    # Generate embeddings
    embeddings = generate_embeddings(chunks)
    ids = [f"chunk_{index}" for index in range(len(chunks))]

    # Store in vector database
    collection = create_collection()

    store_embeddings(
        collection=collection,
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
    )

    # Retrieve relevant chunks
    query_embedding = generate_query_embedding(query)

    results = query_collection(
        collection=collection,
        query_embedding=query_embedding,
        n_results=n_results,
    )

    retrieved_chunks = results["documents"][0]
    context = "\n\n".join(retrieved_chunks)

    # Build prompt
    prompt = prompt_template.format(
        context=context,
        query=query,
    )

    # Generate answer
    try:
        response = generate_content(prompt)
    except Exception as error:
        print(f"Gemini request failed: {error}")

        return {
            "question": query,
            "retrieved_chunks": retrieved_chunks,
            "context": context,
            "answer": None,
            "error": str(error),
        }

    return {
        "question": query,
        "retrieved_chunks": retrieved_chunks,
        "context": context,
        "answer": response.text,
    }