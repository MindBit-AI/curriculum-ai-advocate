# Embedding Homework Assignment

## Overview

This assignment focuses on using OpenAI's embedding API to convert text into numeric vectors, which can then be used for semantic similarity search. You'll be completing the `get_embedding` function to generate embeddings for text documents, and then see how these can be used for simple semantic search.

## Requirements

- OpenAI API key (set as environment variable `OPENAI_API_KEY`)
- Python packages: `openai`, `faiss-cpu`, `numpy`

## Instructions

1. Navigate to the `start` folder where you'll find a partially completed implementation in `main.py`
2. Complete the `get_embedding` function by implementing the OpenAI embedding functionality
3. The function should:
   - Create an OpenAI client
   - Call the embeddings API with the `text-embedding-3-small` model
   - Return the embedding vector from the response
4. Run the script to see if your implementation correctly identifies the movie that best matches the query

## Expected Output

When implemented correctly, the script should identify "The Shawshank Redemption" as the most relevant text for the query "Tell me about a prison movie".

## Documentation

- OpenAI Embeddings API: https://platform.openai.com/docs/guides/embeddings

## Getting Started

To install the required packages:

```bash
pip install openai faiss-cpu numpy
```

Make sure your OpenAI API key is set:

```bash
# For Mac/Linux
export OPENAI_API_KEY=your_api_key_here

# For Windows (Command Prompt)
set OPENAI_API_KEY=your_api_key_here

# For Windows (PowerShell)
$env:OPENAI_API_KEY="your_api_key_here"
```

## Solution

A complete solution is provided in the `solution` folder for reference. 