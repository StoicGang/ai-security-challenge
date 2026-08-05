from google import genai
from config import GEMINI_API_KEY, GENAI_MODEL_NAME
from common.chunking import chunk_document, read_document
from common.embedding import generate_embeddings, generate_query_embedding
from common.vector_db import create_collection, store_embeddings, query_collection
from common.prompts import RAG_PROMPT

def run_rag(
        document_path, 
        query, 
        n_results=2,
        prompt_template=RAG_PROMPT
):
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
    
    query_embedding = generate_query_embedding(query)

    results = query_collection(
        collection=collection,
        query_embedding=query_embedding,
        n_results=n_results,
    )

    retrieved_chunks = results["documents"][0]

    context = "\n\n".join(retrieved_chunks)

    prompt = prompt_template.format(
        context = context,
        query=query,
    )
    
    # gemini client 
    client = genai.Client(api_key=GEMINI_API_KEY)

    # send response 
    response = client.models.generate_content(
        model=GENAI_MODEL_NAME,
        contents=prompt,
    )
    
    return {
        "question": query,
        "retrieved_chunks": retrieved_chunks,
        "context": context,
        "answer": response.text,
    }