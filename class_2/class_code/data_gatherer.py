from langchain_community.vectorstores import Pinecone
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

def load_documents():
    "Load all text documents from the letters directory."
    pass

def chunk_documents(docs):
    "Split documents into smaller chunks for better processing."
    pass

def embed_documents(docs, namespace):
    "Embed documents and place them in the vector store"
    pass

def search_documents(query, namespace):
    "Search the vector store with the user query"
    pass

if __name__ == "__main__":


    # prompt_template = ChatPromptTemplate.from_messages([
    #     (
    #         "system", 
    #         """Provide an answer to the user's query about Berkshire Hathaway.
    #             Documents from the Berkshire Hathaway shareholder meetings will be provided.
    #             Use those documents to best answer the question.
    #         """
    #     ),
    #     (
    #         "system",
    #         "Documents: {docs}"
    #     ),
    #     (
    #         "user",
    #         "{query}"
    #     )
    # ])
    # prompt = prompt_template.invoke({"docs": docs, "query": user_query})
