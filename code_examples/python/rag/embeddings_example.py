from langchain_community.document_loaders import SitemapLoader
from openai import OpenAI
import numpy as np
import faiss

# Initialize OpenAI client
client = OpenAI()

def get_embedding(text):
    """Get embeddings for a single text using OpenAI"""
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

# Example documents about movies
documents = [
    "The Shawshank Redemption is a story about hope and friendship",
    "The Godfather is a classic mafia crime drama",
    "Inception explores dreams within dreams"
]

# Convert documents to embeddings
print("Converting documents to embeddings...")
embeddings = []
for doc in documents:
    embedding = get_embedding(doc)
    embeddings.append(embedding)

# Initialize FAISS index
dimension = len(embeddings[0])  # Get dimension of embeddings
index = faiss.IndexFlatL2(dimension)  # Using L2 (Euclidean) distance

# Add embeddings to FAISS index
print("Adding embeddings to FAISS index...")
index.add(np.array(embeddings, dtype='float32'))

# Perform similarity search
query = "Tell me about prison movies"
print(f"\nSearching for: '{query}'")

# Get query embedding and search
query_embedding = get_embedding(query)
k = len(documents)  # Number of nearest neighbors to retrieve
distances, indices = index.search(np.array([query_embedding], dtype='float32'), k)

# Print results
print("\nSearch Results:")
print("-" * 50)
for i in range(k):
    print(f"Match {i+1} (Distance: {distances[0][i]:.4f}):")
    print(documents[indices[0][i]])
    print() 

# Fun insight:
# These two texts get converted to embeddings:
text1 = "The Shawshank Redemption is a story about hope and friendship"
text2 = "Tell me about prison movies"

# Even though text1 doesn't contain the word "prison", the OpenAI embedding model:
# - Knows "Shawshank Redemption" is strongly associated with prisons
# - Understands this is a prison-related movie
# - Places these embeddings close together in vector space