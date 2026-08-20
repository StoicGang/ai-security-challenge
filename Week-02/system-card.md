# System Card: Week 2 RAG Component

## Intended Use

This RAG component was created as an experimental system for learning and testing RAG and AI security principles. It is operated by the developer and uses a fixed, self-authored article as its retrieval corpus. The RAG pipeline retrieves relevant context from the corpus and provides that context to a downstream LLM. The system does not guarantee that retrieved content is factually correct, as the quality of the response depends partly on the quality and accuracy of the source corpus.

## Known Risks

### Corpus Integrity and Poisoning

If an unauthorized party modifies the retrieval corpus, malicious content may be retrieved and passed directly to the downstream LLM. The LLM may treat the malicious content as trusted context, causing its output to be influenced by attacker-controlled information and potentially producing incorrect or unsafe results.

### Retrieval Failure

Relevant information may exist in the corpus but fail to be retrieved because of limitations or configuration issues in the retrieval pipeline. This can result in irrelevant or insufficient context being provided to the downstream LLM, potentially causing an incorrect or incomplete response.

### Source Data Quality

The retrieval pipeline can correctly retrieve a chunk that contains inaccurate, incomplete, or outdated information. Because the downstream LLM receives this content as context, it may rely on the incorrect information and produce a response containing false or misleading claims.

### Retrieved-Content Instruction Injection

Retrieved documents may contain instruction-like content that influences the downstream LLM. If the downstream system does not appropriately distinguish retrieved data from instructions, the model may follow or be influenced by those instructions rather than treating the retrieved content solely as reference material.

## Responsible Party

The developer and sole operator of this experimental system is responsible for maintaining the integrity and quality of the retrieval corpus, including ensuring that the source material is appropriate and protected from unauthorized modification.

The developer is also responsible for maintaining a consistent and correctly configured retrieval pipeline, including document chunking, embedding generation, indexing, and similarity-based retrieval.

The developer is responsible for the downstream integration of retrieved context with the LLM and for applying appropriate controls to prevent untrusted retrieved content from being treated as instructions or being used to perform unauthorized operations.
