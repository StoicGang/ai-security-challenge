from config import (
    file_path,
    DEFAULT_CHUNK_SIZE,
    DEFAULT_OVERLAP,
    GEMINI_API_KEY,
    GENAI_MODEL_NAME,
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

from  google import genai 

def main():
    document_path = file_path(
        week=2,
        day=9,
        filename="article.md"
    )
    document = read_document(document_path)
    chunks = chunk_document(document)
    embeddings = generate_embeddings(chunks)
    ids = [f"chunk_{i}" for i in range(len(chunks))]
    collection = create_collection()

    store_embeddings(
        collection=collection,
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        )

    query = "What is the formula for the FGSM? What each field tells?"

    query_embedding = generate_query_embedding(query)

    results = query_collection(collection=collection,
                               query_embedding=query_embedding,
                               n_results=5,
                               )

    retrieved_chunks = results["documents"][0]

    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
    You are a helpful AI assistant with expertise in AI and Cybersecurity.

    Answer the user's question using ONLY the provided context.

    If the context does not contain enough information, reply:
    "I don't know based on the provided context."

    Context:
    {context}

    Question:
    {query}

    Answer:
    """

    # gemini client 
    client = genai.Client(api_key=GEMINI_API_KEY)

    # send response 
    response = client.models.generate_content(
        model=GENAI_MODEL_NAME,
        contents=prompt,
    )

    print("\nQuestion:")
    print(query)

    print("\nRetrieved Context:")
    print(context)

    print("\nGrounded Answer:")
    print(response.text)

if __name__ == "__main__":
    main()