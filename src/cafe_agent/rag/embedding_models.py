from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from my_keys import GEMINI_API_KEY

embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=GEMINI_API_KEY
)

embedding_model2 = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")