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

### 3. LangSmith Setup (for Observability)

1. Sign up for a free account at [LangSmith](https://smith.langchain.com/)
2. Create a new API key:
   - Navigate to Settings > API Keys
   - Create a new API key and copy it
3. Set up environment variables:
   - `LANGCHAIN_API_KEY=your_langsmith_api_key_here`
   - `LANGCHAIN_PROJECT=rag-observability` (or any project name you prefer)

## Assignment Instructions

1. The `start` folder contains a basic implementation with a TODO section in the `search_documents` function.
2. Your task is to implement the missing Pinecone query functionality by following the documentation linked in the comments.
3. Once completed, your code should be able to search for relevant documents and generate answers based on those documents.

## Requirements

- OpenAI API key (set as environment variable `OPENAI_API_KEY`)
- Pinecone API key (set as environment variable `PINECONE_API_KEY`)
- Pinecone index with the same name as specified in the code (default is "test")
- LangSmith API key (set as environment variable `LANGCHAIN_API_KEY`)

## Testing

1. First uncomment and run the document loading and embedding code (first-time setup)
2. Then test with the provided query or create your own questions
3. Visit your LangSmith dashboard to view detailed traces of your RAG pipeline execution

## Documentation

- Pinecone documentation: https://sdk.pinecone.io/python/pinecone/grpc.html#GRPCIndex.query
- LangSmith documentation: https://docs.smith.langchain.com

## Solution

A complete solution is provided in the `solution` folder for reference.

## Observability with LangSmith

The code has been instrumented with LangSmith for observability. This provides:

1. Tracing of all RAG pipeline steps
2. Detailed metrics for each component (embeddings, vector search, LLM calls)
3. Input/output captures for debugging
4. Performance monitoring

To view your traces:
1. Log in to your LangSmith account
2. Navigate to the project you specified in your environment variables
3. You'll see a list of all executions with their status, duration, and other metrics
4. Click on any run to see the detailed trace with inputs, outputs, and execution time for each step 