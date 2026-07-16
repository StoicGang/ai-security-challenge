from config import (
    file_path,
    DEFAULT_CHUNK_SIZE,
    DEFAULT_OVERLAP,
)

from common.chunking import (
    read_document,
    chunk_document,
)

from common.embedding import (
    generate_embeddings,
    generate_query_embedding,
)

from common.vector_db import (
    create_collection,
    store_embeddings,
    query_collection,
)


def main():
    # Read document
    document_path = file_path(
        week=2,
        day=9,
        filename="article.md"
    )

    document = read_document(document_path)

    # Chunk document
    chunks = chunk_document(
        document=document,
        chunk_size=DEFAULT_CHUNK_SIZE,
        overlap=DEFAULT_OVERLAP,
    )

    print(f"Generated {len(chunks)} chunks.")

    # Generate embeddings
    embeddings = generate_embeddings(chunks)

    # Generate IDs
    ids = [f"chunk_{i}" for i in range(len(chunks))]

    # Create collection
    collection = create_collection()

    # Store embeddings
    store_embeddings(
        collection=collection,
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
    )

    print("Stored successfully.")

    # Query
    query = input("Enter the query: ")

    query_embedding = generate_query_embedding(query)

    results = query_collection(
        collection=collection,
        query_embedding=query_embedding,
        n_results=2,
    )

    # Display results
    print(f"\nQuery:\n{query}")
    print("\nTop 2 Results:\n")

    retrieved_ids = results["ids"][0]
    documents = results["documents"][0]
    distances = results["distances"][0]

    for i, (doc_id, document, distance) in enumerate(
        zip(retrieved_ids, documents, distances),
        start=1,
    ):
        print(f"Result {i}")
        print(f"ID: {doc_id}")
        print(f"Distance: {distance:.4f}")
        print(document[:300] + "...")
        print("-" * 60)


if __name__ == "__main__":
    main()