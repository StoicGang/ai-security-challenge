# ML Supply Chain Checklist

**Project:** AI Security Mastery Challenge Project

**Purpose:** Evaluate the trustworthiness, reproducibility, and maintainability of the ML supply chain used in this project.

| Sr. No. | Checklist Item                                                                                                                                 | Evidence to Verify                                                                                                              | Current Status                                                                                                                                    |
| :-----: | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|    1    | **The project records every external AI model it depends on, including the model name, publisher, version/revision, source URL, and license.** | A dedicated `MODEL.md` listing every AI model used by the project.                        | **Fail** – No dedicated model inventory currently exists.                                                                                         |
|    2    | **Python dependencies are pinned to specific versions to ensure reproducible builds.**                                                         | `requirements.txt`, `pyproject.toml`, or a lock file with explicit version pinning.                                             | **Fail** – Dependencies are not consistently pinned to exact versions.                                                                            |
|    3    | **Every external AI model is obtained from an official or trusted source, and its provenance can be verified.**                                | Official Hugging Face model page, model card, or official provider documentation referenced in the project.                     | **Partial** – Models are obtained from trusted providers, but their provenance is not formally documented within the project.                     |
|    4    | **External AI services used by the project (e.g., Gemini) are documented with their provider and exact model identifier.**                     | Configuration files or project documentation showing the provider and exact model identifier (e.g., `models/gemini-3.5-flash`). | **Partial** – The configuration contains the model identifier, but supporting documentation about the provider and model selection is incomplete. |
|    5    | **The project defines a documented review process before updating AI models or major ML dependencies.**                                        | Changelog, update policy, or review notes describing how AI component updates are evaluated before adoption.                    | **Fail** – No documented review or approval process currently exists.                                                                             |

## Summary

* **Pass:** 0
* **Partial:** 2
* **Fail:** 3

## Future Improvements

* Create a `MODEL.md` file that inventories every external AI model used by the project.
* Record the official model repository URL, publisher, version/revision, and license for each model.
* Pin all Python dependencies to exact versions to ensure reproducible builds.
* Document external AI providers and the rationale for selecting each model.
* Establish a review process for updating AI models and ML dependencies, including provenance verification before adoption.
