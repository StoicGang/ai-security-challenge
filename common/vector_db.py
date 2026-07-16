import chromadb

from config import COLLECTION_NAME


def create_collection():

    client = chromadb.Client()

    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass

    return client.create_collection(
        name=COLLECTION_NAME
    )


def store_embeddings(
    collection,
    ids,
    documents,
    embeddings
):

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings
    )


def query_collection(
    collection,
    query_embedding,
    n_results=2
):

    return collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )