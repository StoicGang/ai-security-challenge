# Week 5 Learning - AI Security Attacks on AI Models

## Core Concepts
---

### Training Data Extraction

Training data extraction is an attack where an attacker interacts with an AI model in an attempt to recover specific pieces of information that the model retained from its training data. Instead of trying to copy the model itself, the attacker tries to make the model reveal sensitive or confidential information that was never intended to be exposed.

> **Remember**: The goal is to recover memorized information, not to steal the model.

### Memorization vs Generalization

A secure AI model should answer questions by applying the patterns it learned rather than repeating exact examples from its training data. When a model reproduces specific training examples instead of generating answers from learned knowledge, it creates a privacy and security risk.

> **Remember**: Learn patterns, don't repeat examples.

## Understanding Check

### What is the difference between training data extraction and model stealing?

Training data extraction focuses on recovering specific pieces of information that the model memorized during training, such as confidential documents, source code, or personal information. The objective is to extract sensitive data from the model.

Model stealing, on the other hand, aims to copy or approximate the model's functionality by observing its outputs. The attacker wants to recreate the model's behavior rather than recover its training data.

> **Remember**: Training data extraction targets the information inside the model. Model stealing targets the model itself.

## Mental Models
---

| Concept | Mental Model |
|---------|--------------|
| Training Data Extraction | Asking someone to recall confidential pages from a book they once studied instead of asking them to explain the topic in their own words. |
| Memorization vs Generalization | Understanding a recipe well enough to cook it versus reciting the recipe word-for-word from memory. |

