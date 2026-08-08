from config import lab_artifact_path
from common.rag_integration import run_rag

def main():
    clean_document = lab_artifact_path("lab_artifact.md")
    poisoned_document = lab_artifact_path("lab_artifact_poisoned.md")

    query = "How does epsilon affect FGSM?"

    clean_result = run_rag(
        document_path=clean_document,
        query=query,
    )

    poisoned_result = run_rag(
        document_path=poisoned_document,
        query=query,
        n_results=3,
    )

    print("\nQuestion:")
    print(query)

    print("\n" + "=" * 25 + " BEFORE " + "=" * 25)
    print("\nRetrieved Chunks:")
    for i, chunk in enumerate(clean_result["retrieved_chunks"], start=1):
        print(f"\nChunk {i}:")
        print(chunk)

    print("\nAnswer:")
    print(clean_result["answer"])

    print("\n" + "=" * 26 + " AFTER " + "=" * 26)
    print("\nRetrieved Chunks:")
    for i, chunk in enumerate(poisoned_result["retrieved_chunks"], start=1):
        print(f"\nChunk {i}:")
        print(chunk)

    print("\nAnswer:")
    print(poisoned_result["answer"])

if __name__ == "__main__":
    main()