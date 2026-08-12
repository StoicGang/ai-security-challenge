from config import lab_artifact_path
from common.rag_integration import run_rag

DOCUMENT_PATH = lab_artifact_path(
    "day038_indirect_injection_02.md"
)

def main():
    query = input("Question: ").strip()

    result = run_rag(
        document_path=DOCUMENT_PATH,
        query=query,
    )

    print("\n=== Retrieved Context ===")
    print(result["context"])

    print("\n=== Agent Answer ===")
    print(result["answer"])


if __name__ == "__main__":
    main()