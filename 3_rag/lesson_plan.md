# RAG

## Introduction

Retrieval Augmented Generation, or RAG, is a big topic in generative AI development and for good reason. RAG is the process of gathering context and injecting it into your prompts. In LLM applications, adding context to prompts dramatically improves the output. Implementing a good RAG system requires careful planning. You'll need to consider what context you'll need, where that context exists, how those documents will be stored and manged so the sytem can access it, and more. You'll likely need to involve some other individuals to help gather everything, and we'll cover some of those leadership strategeis as well. By the end, you'll have a good idea about what your RAG system could look like. You may even start seeing why we like to say "context is king".

## Core Competencies

Provides context that LLM wasn’t trained on
Document database creation and text retrieval
Injects company-specific insights and expertise
Expands LLM knowledge base and improves accuracy
Topics covered:
Embeddings and their function
Chunking strategies for document preparation
Vector databases and options available
Storing documents in vector DBs
End-to-end RAG implementation
Similarity search and strategies
Prompt examples and summary lookup

Examples:
File ingestion and configuration
Document indexer and lookup

### The student must demonstrate...

1. How to setup a vector database
2. Embedding documents
3. Chunk documents effectively
4. Gather context and inject it into your prompt
5. Know various RAG strategies and how to decide which one to choose

## Coding Problems

**1. The Types of RAG systems**

   - **Core Competency:** Understanding the different types of RAG systems, such as simple retrieval, document retrieval, and summary retrieval.
   
   - **Relevance:** 
      - Understanding the general process of RAG helps you as the engineer know where it goes in your process. This is especially important when deciding which type of RAG system to use for a particular project.

   - **Procedure:**
      1. Go over the idea that RAG is simply providing context. Context is information pertaining to a given problem. That context can come from anywhere: document, database, websites, etc. We'll be covering documents today because it's the most novel use case, and a powerful one at that. We have never been able to leverage unstructured context like this before. 
         - Rag is simply gathering content to add to your prompt
      2. High level:
         - you need documents you want to search
         - you need a vector database to store and search the documents 
         - you need to return the best results and inject them into your prompt
      4. Code:
         - Diagram of RAG instead of code

**2. Setting up a Vector Database with Pinecone**

   - **Core Competency:** Understanding how to set up a vector database with Pinecone, including naming the index, what the index will contain, and how to store data in it.
   
   - **Relevance:**
      - Pinecone is a popular vector database that can be used for RAG. Setting up a Pinecone vector database is an essential step in implementing a RAG system.

   - **Procedure:**
      1. Set up an index in Pinecone using the website
      2. Discuss how to data is stored in pinecone: as numbers

**3. Embedding documents and storing them into Pinecone**

   - **Core Competency:** Understanding how to embed documents and store them in a Pinecone vector database.
   
   - **Relevance:**
      - Embedding documents is an essential step in RAG. This involves converting the document text into a numerical representation that can be stored in a vector database.

   - **Procedure:**
      1. Explain how embeddings work, including the process of tokenization and encoding.
      2. Show how to embed documents using code (e.g., Python).
      3. Discuss how to store the embedded document in Pinecone.

**4. Chunking documents effectively**

   - **Core Competency:** Understanding different chunking strategies for documents, such as character-based chunking and semantic chunking.
   
   - **Relevance:**
      - Chunking a document makes it easier to find the most prevalent information you need. Many chunking strategies exist, and you want to be aware of them to know how to address your use case.

   - **Procedure:**
      1. Explain different chunking strategies for documents, including character-based chunking and semantic chunking.
      2. Discuss how to decide which chunking strategy is best for a particular project.
      3. Code:
         - Example code for using chunking strategies in Python

**5. Gather context and inject it into your prompt**

   - **Core Competency:** Understanding how to gather context from documents, summaries, or chunks and inject them into the prompt using RAG.
   
   - **Relevance:**
      - This is the final step in the RAG process. You need to gather context from documents, summaries, or chunks and inject it into the prompt.

   - **Procedure:**
      1. Explain how to gather context from documents, summaries, or chunks using code (e.g., Python).
      2. Discuss how to decide which type of context to use for a particular project.
      3. Code:
         - Example code for using RAG in Python
      4. Show how much RAG improved a result by showing an evaluation with and without RAG
    


### Challenge 1: 

**Objective:** 

## Conclusion

