# AI Audit Summary

## System

**System:** Week 2 RAG Component

This is an experimental RAG system operated and maintained by the developer. It uses a fixed, self-authored retrieval corpus and passes retrieved context to a downstream LLM.

## Intended Use

The component was developed for experimentation and learning around RAG and AI security principles. The current retrieval source is fixed and developer-controlled, and no attacker-controlled modification path has been demonstrated.

## Assessed Risk

**Risk:** Retrieved content may contain attacker-controlled instructions that influence model behavior.

The system card identifies retrieved-content instruction injection as a known risk. Retrieved documents may contain instruction-like content that the downstream LLM could interpret as instructions rather than solely as reference material.

## Risk Assessment

| Field | Assessment | Reasoning |
|---|---|---|
| **Likelihood** | **Low** | The current retrieval corpus is fixed, self-authored, and developer-controlled. No attacker-controlled modification path has been demonstrated. |
| **Impact** | **Low** | The demonstrated consequence is unintended model output or behavior. No sensitive-data access or state-changing capability was demonstrated. |
| **Mitigation** | Runtime logging | Week 6 runtime logging records tool names and inputs, improving observability and supporting detection and investigation. |
| **Residual Risk** | **Low** | Logging improves observability but does not prevent retrieved-content injection. The underlying risk therefore remains if an attacker can modify or introduce content into the retrieval corpus. |

## Risk Context

The current low assessment applies to the experimental deployment and its demonstrated attack surface. The underlying risk remains relevant because a compromise of the retrieval corpus could allow malicious content to reach the downstream LLM and influence its behavior.

If the same architecture were deployed in a production environment with additional users, sensitive data, or attacker-accessible content sources, the likelihood and/or impact assessment would need to be reassessed.

## Framework Reference

**NIST AI RMF:** Provides a framework for managing risks associated with AI systems and provides governance context for identifying, assessing, and managing AI risks.

## Audit Conclusion

The Week 2 RAG component has a documented risk of retrieved-content instruction injection. The current risk is assessed as low because the retrieval corpus is fixed and developer-controlled and the demonstrated impact is limited. Runtime logging provides observability but does not eliminate the underlying risk. The assessment should be revisited if the system's deployment context, data sources, access controls, or capabilities change.