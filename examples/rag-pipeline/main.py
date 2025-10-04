from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_anthropic import ChatAnthropic
from langchain.chains import RetrievalQA
from langchain_core.documents import Document

load_dotenv()

# 1. Initialize embeddings + Claude LLM
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
llm = ChatAnthropic(model="claude-3-sonnet-20240229", temperature=0)

# 2. Example documents
docs = [
    Document(page_content="The Eiffel Tower is located in Paris, France."),
    Document(page_content="The Great Wall of China is visible from space only under special conditions."),
    Document(page_content="LayerZero is an interoperability protocol for blockchains."),
]

# 3. Build FAISS vectorstore
db = FAISS.from_documents(docs, embeddings)

# 4. Setup retriever + RAG pipeline
retriever = db.as_retriever()
qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# 5. Run a query
query = "Where is the Eiffel Tower?"
response = qa.run(query)

print("Q:", query)
print("A:", response)
