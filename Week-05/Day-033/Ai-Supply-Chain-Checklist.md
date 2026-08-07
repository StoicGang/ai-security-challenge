# AI Project Supply Chain Security Checklist

## Purpose

Evaluate the trustworthiness, reproducibility, and maintainability of the AI supply chain used in an AI or ML project.

## How to Use This Checklist

1. Review each applicable checklist item.
2. Collect evidence before assigning a status.
3. Record one of the following statuses:
   - Pass
   - Partial
   - Fail
   - N/A (Not Applicable)
4. Repeat the review whenever introducing or updating a dependency.

## 1. AI Models
---
| Sr. No. | Checklist Item                                                                                                        | Evidence to Verify                                                               | Current Status              |
| :-----: | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | --------------------------- |
|   1.1   | Every AI model used by the project is documented with its name, publisher, version/revision, source URL, and license. | `MODEL.md`, model card, official repository.                                     | Pass / Partial / Fail / N/A |
|   1.2   | Each AI model is obtained from an official or trusted source, and its provenance can be verified.                     | Official Hugging Face page, vendor documentation, signed release (if available). | Pass / Partial / Fail / N/A |
|   1.3   | The project documents why each AI model was selected.                                                                 | Project documentation, architecture notes, design decisions.                     | Pass / Partial / Fail / N/A |
|   1.4   | The exact model version or revision is pinned to ensure reproducibility.                                              | Configuration files, model revision hash, commit ID, or version tag.             | Pass / Partial / Fail / N/A |
|   1.5   | A documented review process exists before updating or replacing AI models.                                            | Change log, pull request, update policy, review notes.                           | Pass / Partial / Fail / N/A |
|   1.6   | The licensing and usage terms of every AI model have been reviewed for compatibility with the project.                | Model license, provider documentation, legal review (if applicable).             | Pass / Partial / Fail / N/A |

## 2. Datasets
---
| Sr. No. | Checklist Item                                                                                    | Evidence to Verify                                                     | Current Status              |
| :-----: | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | --------------------------- |
|   2.1   | Every dataset used by the project is documented with its name, source, version, and license.      | `DATASET.md`, dataset documentation, official repository.              | Pass / Partial / Fail / N/A |
|   2.2   | Each dataset is obtained from an official or trusted source, and its provenance can be verified.  | Official dataset page, publisher documentation, trusted repository.    | Pass / Partial / Fail / N/A |
|   2.3   | The integrity of downloaded datasets can be verified before use.                                  | SHA256 checksum, digital signature, or hash published by the provider. | Pass / Partial / Fail / N/A |
|   2.4   | The project documents why each dataset was selected and its intended purpose.                     | Project documentation, design notes, architecture documentation.       | Pass / Partial / Fail / N/A |
|   2.5   | The dataset version or release is recorded to ensure reproducibility.                             | Dataset version, release tag, commit hash, or snapshot identifier.     | Pass / Partial / Fail / N/A |
|   2.6   | The dataset license and usage restrictions have been reviewed for compatibility with the project. | Dataset license, terms of use, provider documentation.                 | Pass / Partial / Fail / N/A |


## 3. Software Dependencies
---
| Sr. No. | Checklist Item                                                                         | Evidence to Verify                                                                                  | Current Status              |
| :-----: | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------- |
|   3.1   | All software dependencies are documented and pinned to specific versions.              | `requirements.txt`, `pyproject.toml`, `package-lock.json`, `poetry.lock`, or equivalent lock files. | Pass / Partial / Fail / N/A |
|   3.2   | Third-party packages are obtained from trusted or official package repositories.       | PyPI, npm, Maven Central, official GitHub repositories, vendor documentation.                       | Pass / Partial / Fail / N/A |
|   3.3   | The project periodically reviews dependencies for known security vulnerabilities.      | Dependency scanning reports, GitHub Dependabot, `pip-audit`, `npm audit`, or similar tools.         | Pass / Partial / Fail / N/A |
|   3.4   | Unused or deprecated dependencies are regularly identified and removed.                | Dependency review, package inventory, project maintenance records.                                  | Pass / Partial / Fail / N/A |
|   3.5   | The purpose of critical third-party dependencies is documented.                        | Architecture documentation, README, dependency inventory.                                           | Pass / Partial / Fail / N/A |
|   3.6   | Dependency updates follow a documented review and testing process before being merged. | Pull requests, changelog, update policy, CI test results.                                           | Pass / Partial / Fail / N/A |


## 4. External AI Services
---
| Sr. No. | Checklist Item                                                                                                           | Evidence to Verify                                                      | Current Status              |
| :-----: | ------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------- | --------------------------- |
|   4.1   | Every external AI service used by the project is documented with its provider, service name, and exact model identifier. | Project documentation, configuration files, provider documentation.     | Pass / Partial / Fail / N/A |
|   4.2   | API credentials are stored securely and never committed to source control.                                               | `.env` files, secret manager, `.gitignore`, CI/CD secret configuration. | Pass / Partial / Fail / N/A |
|   4.3   | The project documents why each external AI service was selected.                                                         | Architecture documentation, design decisions, README.                   | Pass / Partial / Fail / N/A |
|   4.4   | The service version, API version, or model identifier is fixed where possible to ensure consistent behavior.             | Configuration files, API documentation, model version settings.         | Pass / Partial / Fail / N/A |
|   4.5   | The project has a documented plan for handling service outages, API changes, or model deprecation.                       | Architecture documentation, fallback strategy, operational runbook.     | Pass / Partial / Fail / N/A |
|   4.6   | Usage limits, pricing, and terms of service have been reviewed before adoption.                                          | Provider documentation, subscription records, project documentation.    | Pass / Partial / Fail / N/A |


## 5. Infrastructure & Deployment
---
| Sr. No. | Checklist Item                                                                                                                                                   | Evidence to Verify                                                                              | Current Status              |
| :-----: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------- |
|   5.1   | All infrastructure components (containers, databases, vector databases, orchestration tools, etc.) are documented with their name, version, source, and purpose. | Deployment documentation, `docker-compose.yml`, Kubernetes manifests, infrastructure inventory. | Pass / Partial / Fail / N/A |
|   5.2   | Container images are obtained from trusted registries and pinned to specific versions or immutable digests.                                                      | `Dockerfile`, container registry, image digest (`sha256`).                                      | Pass / Partial / Fail / N/A |
|   5.3   | CI/CD workflows use trusted actions, plugins, or runners that are pinned to specific versions or commit SHAs.                                                    | GitHub Actions workflows, CI/CD configuration files.                                            | Pass / Partial / Fail / N/A |
|   5.4   | Infrastructure configuration is version-controlled and reviewed before deployment.                                                                               | Git repository, pull requests, infrastructure-as-code files.                                    | Pass / Partial / Fail / N/A |
|   5.5   | Deployment secrets and sensitive configuration values are stored securely and are not hardcoded.                                                                 | Secret manager, `.env`, CI/CD secrets, deployment configuration.                                | Pass / Partial / Fail / N/A |
|   5.6   | A documented process exists for updating and patching infrastructure components.                                                                                 | Maintenance policy, change log, patch management documentation.                                 | Pass / Partial / Fail / N/A |


## 6. Governance
---
| Sr. No. | Checklist Item                                                                                                                                                      | Evidence to Verify                                                                             | Current Status              |
| :-----: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | --------------------------- |
|   6.1   | The project maintains a complete inventory of AI supply chain components, including models, datasets, software dependencies, external services, and infrastructure. | Architecture documentation, inventory files (`MODEL.md`, `DATASET.md`), project documentation. | Pass / Partial / Fail / N/A |
|   6.2   | Roles and responsibilities for maintaining AI supply chain components are clearly defined.                                                                          | `CODEOWNERS`, team documentation, project governance documents.                                | Pass / Partial / Fail / N/A |
|   6.3   | The project has a documented process for reviewing new third-party dependencies before adoption.                                                                    | Dependency review policy, pull requests, architecture review records.                          | Pass / Partial / Fail / N/A |
|   6.4   | The AI supply chain is periodically reviewed for outdated, vulnerable, or untrusted components.                                                                     | Security audit reports, dependency scan reports, review logs.                                  | Pass / Partial / Fail / N/A |
|   6.5   | Security incidents affecting supply chain components are tracked and documented until resolved.                                                                     | Issue tracker, incident reports, vulnerability management records.                             | Pass / Partial / Fail / N/A |
|   6.6   | The checklist is reviewed and updated whenever significant AI technologies or project dependencies change.                                                          | Revision history, changelog, documented review schedule.                                       | Pass / Partial / Fail / N/A |

## Summary

This checklist provides a structured approach to auditing the security, trustworthiness, and reproducibility of an AI project's supply chain. By evaluating AI models, datasets, software dependencies, external AI services, infrastructure, and governance practices, developers can identify potential risks before they impact the project.

The checklist is intended to be used throughout the project lifecycle, especially when introducing new dependencies, updating existing components, or preparing a project for release.

---

## Recommended Improvements

To strengthen the security and reproducibility of an AI project's supply chain, consider adopting the following practices:

* Maintain a complete inventory of all AI models, datasets, external services, software dependencies, and infrastructure components.
* Pin dependency versions and use lock files to produce reproducible builds.
* Verify the provenance, integrity, and licensing of all third-party artifacts before adoption.
* Document the rationale for selecting external models, datasets, and services.
* Review and test dependency updates before integrating them into the project.
* Generate and maintain a **Software Bill of Materials (SBOM)** to improve transparency, compliance, and vulnerability management.
* Regularly audit the supply chain for outdated, vulnerable, or untrusted components.
* Secure secrets and API credentials using dedicated secret management solutions instead of storing them in source code.

### Example Best Practices

**Dependency locking**

Update dependency definitions and regenerate the lock file before releasing new versions to ensure reproducible builds.

```bash
pip-compile --generate-hashes --allow-unsafe requirements.in
```

**Software Bill of Materials (SBOM)**

Regenerate the SBOM whenever dependencies change to maintain an accurate inventory of software components.

```bash
cyclonedx-py requirements requirements.txt -o bom.json
```
