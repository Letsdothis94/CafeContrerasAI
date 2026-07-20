from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.cafe_agent.rag.loader import load_documents

documentos = load_documents("./documents")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1200,
    chunk_overlap=200
)

# chunks = splitter.split_documents(documentos)

# for chunk in chunks:
#     print(chunk)
#     print("-----" * 10)