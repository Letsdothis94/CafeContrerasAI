from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from my_keys import GEMINI_API_KEY
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0,
    google_api_key=GEMINI_API_KEY
)

# r = llm.invoke("Explica RAG en un parrafo corto.")
# print(r.content)