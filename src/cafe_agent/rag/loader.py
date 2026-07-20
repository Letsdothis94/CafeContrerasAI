from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader

def load_documents(directory: str):
    documentos = []

    for doc in Path(directory).glob("*.pdf"):
        try:
            loader = PyMuPDFLoader(str(doc))
            documentos.extend(loader.load())
            print(f"Documento cargado: {doc.name}")
    
        except Exception as e:
            print(f"Error cargando documento: {doc.name}: {e}")

    print(f"Documentos disponibles por ahora: {len(documentos)}")

    return documentos