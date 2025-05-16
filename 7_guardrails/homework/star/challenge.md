# Advanced Guardrails Challenge

## Challenge Overview

In this challenge, you'll extend the basic PII guardrails implementation to create a more comprehensive system for responsible LLM development.

## Tasks

### 1. Multi-Layer Guardrail System

Create a unified guardrail system that can incorporate multiple types of guardrails:

- PII Protection (extending the base implementation)
- Content Moderation (detecting and filtering inappropriate or harmful content)
- Topic Boundaries (keeping conversations within approved domains)
- Jailbreak Detection (preventing prompt injection attacks)

### 2. Advanced PII Detection

Improve the PII detection by:

- Adding support for international PII formats (EU National IDs, passports, etc.)
- Implementing contextual PII detection (understanding when things like names appear in context)
- Creating confidence levels for PII detection to reduce false positives

### 3. Configurable Response Strategies

Implement different response strategies when guardrails are triggered:

- Complete blocking (as in the base implementation)
- Redaction with replacement tokens
- Guided refactoring (helping users reformulate their query)
- Logging and monitoring without blocking (for less sensitive scenarios)

### 4. Evaluation Framework

Design a system to measure the effectiveness of your guardrails:

- Create test cases for each guardrail type
- Implement metrics for precision, recall, and false positive rates
- Build a visualization dashboard for guardrail performance

## Implementation Tips

1. Start by understanding the base PII implementation in the solution folder
2. Modularize your code to allow for easy addition of new guardrail types
3. Consider using existing libraries where appropriate (e.g., for toxicity detection)
4. Balance strictness with usability - overly strict guardrails can frustrate users

## Bonus Challenge

Implement a "guardrail explanation" feature that provides clear, educational feedback to users when their requests are blocked or modified, helping them understand why certain information can't be processed and suggesting better alternatives. 