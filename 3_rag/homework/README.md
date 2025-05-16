# RAG Homework Assignment

This folder contains starter code for implementing a Retrieval-Augmented Generation (RAG) system.

## Setup Instructions

### 1. Pinecone Setup

1. Sign up for a free account at [Pinecone](https://www.pinecone.io/)
2. Create a new index:
   - Choose a name for your index (e.g., "class_documents" or "test")
   - Under configuration, select the OpenAI "text-embedding-3-small" embedding model
   - This is OpenAI's most cost-effective embedding model for vector search
3. Get your API key:
   - Click on "API keys" in the left navigation menu
   - You'll see your API keys listed on this page
   - Copy the API key you want to use
4. Set up your environment variable:
   - Add the following to your environment: `PINECONE_API_KEY=your_api_key_here`
   - For Mac/Linux: Run `export PINECONE_API_KEY=your_api_key_here` in your terminal
   - For Windows: Run `set PINECONE_API_KEY=your_api_key_here` in Command Prompt or `$env:PINECONE_API_KEY="your_api_key_here"` in PowerShell

### 2. OpenAI Setup

- Set up your OpenAI API key as an environment variable: `OPENAI_API_KEY=your_openai_api_key`

## Assignment Instructions

1. The `start` folder contains a basic implementation with a TODO section in the `search_documents` function.
2. Your task is to implement the missing Pinecone query functionality by following the documentation linked in the comments.
3. Once completed, your code should be able to search for relevant documents and generate answers based on those documents.

## Requirements

- OpenAI API key (set as environment variable `OPENAI_API_KEY`)
- Pinecone API key (set as environment variable `PINECONE_API_KEY`)
- Pinecone index with the same name as specified in the code (default is "test")

## Testing

1. First uncomment and run the document loading and embedding code (first-time setup)
2. Then test with the provided query or create your own questions

## Documentation

- Pinecone documentation: https://sdk.pinecone.io/python/pinecone/grpc.html#GRPCIndex.query

## Solution

A complete solution is provided in the `solution` folder for reference. 