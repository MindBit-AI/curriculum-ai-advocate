from langchain_community.vectorstores import Pinecone
from langchain_community.document_loaders import DirectoryLoader, TextLoader, WebBaseLoader
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

# 3.1
embedding = OpenAIEmbeddings(model='text-embedding-3-small')
index_name = "berkshire-hathaway-class"

# 1.2
def load_documents():
    loader = DirectoryLoader("./", glob="**/letters/*.txt", loader_cls=TextLoader)
    docs = loader.load()

    print(f"Found {len(docs)} letters")
    return docs

#2.1
def chunk_documents(docs):
    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    chunks = text_splitter.split_documents(docs)
    return chunks

def create_summaries(docs):
    llm = ChatOpenAI(model="gpt-4o-mini")
    for doc in docs:
        messages = [
                SystemMessage(content="Create a concise summary of the following document. Include a list of the companies that they invested in this year:"),
                HumanMessage(content=doc.page_content)
            ]
        summary = llm.invoke(messages)
        doc.page_content = summary.content
#3.2
def embed_documents(docs, namespace):
    "embed documents and place them in the vector store"
    PineconeVectorStore.from_documents(
        documents=docs,
        embedding=embedding,
        index_name=index_name,
        namespace=namespace
    )

def search_document_chunks(query, namespace):
    vector_store = PineconeVectorStore(index_name=index_name, embedding=embedding)
    docs = vector_store.similarity_search_with_score(query=query, k=5, namespace=namespace)
    return docs


if __name__ == "__main__":
    # Load chunks 1.3
    # docs = load_documents()

    #Chunks 2.2
    # chunks = chunk_documents(docs=docs)
# 
    #3.3
    # embed_documents(docs=chunks, namespace="chunks")

    #Summaries - Part 2
    # create_summaries(docs)
    # embed_documents(docs=docs, namespace="summaries")

    #Easy query
    user_query = "When did Berkshire Hathaway purchase it's first coke stock?" # should return 1988

    #Harder query
    # user_query = "What stocks did Bershire Hathaway have in 1992?" # Will struggle to return this

    #Search for scores
    docs_and_scores = search_document_chunks(query=user_query, namespace="chunks")
    docs = []
    for doc, score in docs_and_scores:
        print(score)
        print(doc.metadata)
        docs.append(doc.page_content)

    #Send docs and query to open ai
    llm = ChatOpenAI(model="gpt-4o-mini", max_tokens=150)
    prompt_template = ChatPromptTemplate.from_messages([
        (
            "system", 
            """Provide an answer to the user's query about Berkshire Hathaway.
                Documents from the Berkshire Hathaway shareholder meetings will be provided.
                Use those documents to best answer the question.
            """
        ),
        (
            "system",
            "Documents: {docs}"
        ),
        (
            "user",
            "{query}"
        )
    ])
    prompt = prompt_template.invoke({"docs": docs, "query": user_query})

    response = llm.invoke(prompt)
    print(response.content)