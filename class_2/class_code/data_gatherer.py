# from langchain_community.vectorstores import Pinecone
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

def load_documents():
    "Load all text documents from the letters directory."
    loader = DirectoryLoader("./", glob="**/letters/*.txt", loader_cls=TextLoader)
    docs = loader.load()

    print(f"Found {len(docs)} letters")
    return docs

def chunk_documents(docs):
    "Split documents into smaller chunks for better processing."
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    chunks = text_splitter.split_documents(docs)
    return chunks

embedding = OpenAIEmbeddings(model='text-embedding-3-small')
index_name = "berkshire-hathaway"

def embed_documents(docs, namespace):
    "Embed documents and place them in the vector store"
    PineconeVectorStore.from_documents(
        documents=docs,
        embedding=embedding,
        index_name=index_name,
        namespace=namespace
    )



def search_documents(query, namespace):
    "Search the vector store with the user query"
    vector_store = PineconeVectorStore(index_name=index_name, embedding=embedding)
    docs = vector_store.similarity_search_with_score(query=query, k=5, namespace=namespace)
    return docs


if __name__ == "__main__":
    # docs = load_documents()
    # chunks = chunk_documents(docs=docs)
    # embed_documents(docs=chunks, namespace="chunks")
    user_query = "When did Berkshire Hathaway purchase it's first coke stock?" # should return 1988
    docs_and_scores = search_documents(query=user_query, namespace="chunks")
    docs = []
    for doc, score in docs_and_scores:
        print(score)
        print(doc.metadata)
        docs.append(doc.page_content)
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
