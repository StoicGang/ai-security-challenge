# Week 5 Learning - AI Security Attacks on AI Models

## STRIDE
## STRIDE

| Category                       | Security Principle                   | Remember It As                                                                      |
| ------------------------------ | ------------------------------------ | ----------------------------------------------------------------------------------- |
| **S — Spoofing**               | **Authentication**                   | **Who are you?** → Someone pretends to be another identity.                         |
| **T — Tampering**              | **Integrity**                        | **Can you change it?** → Someone modifies data or system state.                     |
| **R — Repudiation**            | **Accountability / Non-repudiation** | **Did you really do it?** → An action cannot be reliably attributed or proven.      |
| **I — Information Disclosure** | **Confidentiality**                  | **Can you see it?** → Information reaches someone who should not see it.            |
| **D — Denial of Service**      | **Availability**                     | **Can you break it?** → Resources are exhausted or the service becomes unavailable. |
| **E — Elevation of Privilege** | **Authorization**                    | **Can you do more?** → Someone gains capabilities beyond what they should have.     |


> **Memory Rule**
>
> **Who are you? → Can you change it? → Did you do it? → Can you see it? → Can you break it? → Can you do more?**
>
> **S → T → R → I → D → E**
>
> **Authentication → Integrity → Accountability → Confidentiality → Availability → Authorization**


## Core Concepts

---

### Training Data Extraction

Training data extraction is an attack where an attacker interacts with an AI model in an attempt to recover specific pieces of information that the model retained from its training data. Instead of trying to copy the model itself, the attacker tries to make the model reveal sensitive or confidential information that was never intended to be exposed.

> **Remember**: The goal is to recover memorized information, not to steal the model.

### Memorization vs Generalization

A secure AI model should answer questions by applying the patterns it learned rather than repeating exact examples from its training data. When a model reproduces specific training examples instead of generating answers from learned knowledge, it creates a privacy and security risk.

> **Remember**: Learn patterns, don't repeat examples.

### Data Poisoning

Data poisoning is an attack where an attacker intentionally inserts false, misleading, or malicious information into data used by an AI system. In training-time poisoning, the attacker tries to influence what the model learns so that the trained model develops unintended behavior.

> **Remember**: Poison the data to influence what the model learns.

### Membership Inference

Membership inference is an attack where an attacker tries to determine whether a specific example was included in a model's training dataset. The attacker is not necessarily trying to recover the example itself, but to establish whether it was part of the training data.

> **Remember**: Was this example in the training set?

### Model Extraction

Model extraction is an attack where an attacker queries a target model repeatedly, observes its input-output behavior, and uses those observations to build a model that approximates the target's functionality.

> **Remember**: Observe the model to reproduce its behavior.

### RAG-Corpus Poisoning

RAG-corpus poisoning occurs when an attacker inserts malicious or misleading content into the knowledge corpus used by a retrieval-augmented generation system. The poisoned content becomes a security risk when it is relevant enough to be retrieved and included in the model's context.

> **Remember**: Poisoned content must reach the retrieved context to influence the answer.

### Retrieval and Top-k Ranking

RAG retrieval selects chunks based on their relevance to the user's query. A poisoned chunk does not automatically influence the model simply because it exists in the corpus. It must score highly enough to survive ranking and enter the top-k retrieved context.

> **Remember**: Poisoning the corpus is not enough; the poison must be retrieved.

### Model Provenance

Model provenance describes where a model came from, which version it is, how it was produced or modified, and what other components or sources contributed to it. Provenance provides evidence that the model being deployed is the model that was intended and helps investigate supply-chain compromises.

> **Remember**: Know where the model came from and what happened to it.

### Artifact Integrity and Authenticity

Artifact integrity verifies whether a model or other AI component has changed relative to a trusted reference, while authenticity and provenance establish whether the artifact actually came from the expected source. Cryptographic hashes can help verify integrity, while signatures and provenance can provide stronger evidence of authenticity.

> **Remember**: Integrity asks "was it changed?"; authenticity asks "did it come from the right source?"

### AI Supply Chain Security

AI supply chain security treats models, datasets, libraries, dependencies, and other AI artifacts as components that must be tracked and verified. Security controls should establish provenance, maintain visibility into dependencies, verify artifacts, and monitor changes according to the risk of the system.

> **Remember**: Don't trust the AI component just because it works.

### Training-time vs Inference-time Attacks

Training-time attacks attempt to influence what the model learns before or during training, such as training-data poisoning. Inference-time attacks interact with an already-trained system, such as training-data extraction, membership inference, model extraction, prompt injection, or RAG-corpus poisoning.

> **Remember**: Training attacks influence what the model learns; inference attacks exploit or influence the deployed model.


## Understanding Check

### What is the difference between training data extraction and model stealing?

Training data extraction focuses on recovering specific pieces of information that the model memorized during training, such as confidential documents, source code, or personal information. The objective is to extract sensitive data from the model.

Model stealing, on the other hand, aims to copy or approximate the model's functionality by observing its outputs. The attacker wants to recreate the model's behavior rather than recover its training data.

> **Remember**: Training data extraction targets the information inside the model. Model stealing targets the model itself.

### What capabilities does an attacker need, and what interaction method is used, to recover memorized training information?
An attacker generally needs an interaction surface that allows them to query the trained model and observe its outputs. In a black-box setting, API or chat access can be sufficient. They do not necessarily need access to the training dataset, model weights, or internal architecture. The attacker uses carefully designed queries to probe whether the model will reproduce information it memorized during training.
The attacker interacts with the model through repeated queries, using prompts designed to elicit memorized sequences or sensitive training information. They observe the outputs and iteratively refine their queries based on what the model reveals.

### How does the position of poisoned content within a document or chunk affect the likelihood of it being retrieved?
There is no universal amount of poisoning required to influence a RAG system. The required amount depends on the retrieval method, chunking strategy, embedding model, reranking, top-k value, corpus composition, and the attacker's objective. A small amount of strategically crafted poisoned content may be sufficient if it is highly relevant to targeted queries and consistently enters the top-k retrieved context. Therefore, the attacker generally wants the smallest practical amount of poisoning that reliably reaches the LLM and produces the desired effect, rather than maximizing the percentage of poisoned data.

### How can I verify the integrity and authenticity of an AI model beyond trusting the hosting platform?
I would establish both the artifact's integrity and its provenance rather than trusting the hosting platform alone. I would obtain the model from a trusted source, record its version and provenance, verify cryptographic hashes against a trusted reference, and where available verify cryptographic signatures or attestations. I would also maintain evidence of where the artifact came from and what dependencies it contains.

### Which supply-chain controls should be mandatory for personal projects versus production-grade AI systems?
The controls should be risk-based. A personal project and a production AI system should not necessarily have identical supply-chain requirements because their data sensitivity, exposure, dependencies, and business impact are different.

Personal project: establish basic trust and visibility.

Production: continuously establish, verify, monitor, and enforce trust across the AI supply chain.

### How is data poisoning different from prompt injection in terms of when the attack happens and who can perform it?
Data poisoning and prompt injection differ primarily in where and when the attacker applies influence. Data poisoning targets the data used during training, so the attacker needs a way to influence the training-data pipeline or dataset before or during training. Prompt injection occurs at inference time, where the attacker uses an input or interaction channel to manipulate the instructions or context presented to the model. RAG-corpus poisoning is a related inference-time attack because the attacker targets the retrieved knowledge source rather than the model's training data.

### Why does model provenance matter the same way dependency provenance does in traditional supply-chain security?
Model provenance matters because an AI model is itself a supply-chain artifact. Just like dependency provenance tells us where a software component came from, which version we have, and whether it was modified, model provenance tells us the model's origin, version, lineage, and modifications. This allows us to establish trust, investigate compromises, and reproduce or verify the model we deployed. Without provenance, a model that appears to work correctly could still be an untrusted or malicious artifact.

### What is a practical, partial mitigation for RAG-corpus poisoning, given perfect mitigation is unrealistic?
A practical partial mitigation for RAG-corpus poisoning is to restrict ingestion to trusted or allowlisted sources and validate content before it enters the corpus. I would also maintain provenance and change history for documents, and use hashes or signatures where practical to detect unauthorized modifications. This does not eliminate poisoning completely, but it reduces the attack surface and makes unauthorized changes easier to detect.

## Mental Models

---

| Concept                        | Mental Model                                                                                                                              |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Training Data Extraction       | Asking someone to recall confidential pages from a book they once studied instead of asking them to explain the topic in their own words. |
| Memorization vs Generalization | Understanding a recipe well enough to cook it versus reciting the recipe word-for-word from memory.                                       |
| Data Poisoning                 | Putting misleading pages into a book before someone studies it, so they learn an attacker-controlled pattern or behavior.                 |
| Membership Inference           | Having a particular page and asking whether that exact page was included in the book the model studied.                                   |
| Model Extraction               | Asking a teacher thousands of questions, recording the answers, and using those examples to build another teacher that behaves similarly. |
| RAG-Corpus Poisoning           | Putting a misleading page into a reference library so that the retrieval system selects it when someone asks a related question.          |
| Model Provenance               | Knowing who produced a model, where it came from, which version it is, and what happened to it before it entered the system.              |
| AI Supply Chain                | Treating models, datasets, dependencies, and other AI artifacts as components that need to be verified rather than trusted by default.    |
| Retrieval Security             | Poisoned content only matters to the final answer if it is relevant enough to survive retrieval and enter the model's context.            |


## Biggest Takeaway

---

Week 5 shifted my perspective from securing only the AI application to also securing the data, models, and components that influence its behavior. I learned that AI systems can be attacked before deployment through poisoned training data or compromised supply-chain components, while inference-time attacks can exploit memorization, retrieval, or model interactions. I also learned that security depends on understanding the complete AI supply chain, including model and data provenance, artifact integrity, and retrieval security. A model should not be trusted simply because it works; the data, dependencies, models, and sources behind it also need to be verified and controlled.
