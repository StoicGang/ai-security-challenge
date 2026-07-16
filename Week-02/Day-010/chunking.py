chunk_size = 1000
overlap = 200
step_size = chunk_size - overlap

Document_PATH = "../Day-009/article.md"

def read_document(document_path):
    with open(document_path, "r", encoding="utf-8") as file:
        return file.read()

def chunk_document(document, chunk_size, overlap):
    step_size = chunk_size - overlap
    chunks = []
    Document_size = len(document)
    for i in range (0, Document_size, step_size):
        chunk = document[i:i + chunk_size]
        chunks.append(chunk)
    
    return chunks

if __name__ == "__main__":
    document = read_document(Document_PATH)

    chunks = chunk_document(
        document,
        chunk_size,
        overlap
    )

    for chunk in chunks:
        print("Chunk:", chunk)
        print("Character Count:", len(chunk))