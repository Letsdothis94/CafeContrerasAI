from langchain_community.vectorstores import FAISS
from src.cafe_agent.rag.embedding_models import embedding_model2
from src.cafe_agent.rag.loader import load_documents
from src.cafe_agent.rag.splitter import splitter

documentos = load_documents("./documents")
chunks = splitter.split_documents(documentos)

vectorStore = FAISS.from_documents(chunks, embedding_model2)

retriever = vectorStore.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"score_threshold": 0.1, "k": 4}
)