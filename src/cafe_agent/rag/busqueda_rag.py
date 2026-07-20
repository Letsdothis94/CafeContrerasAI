from src.cafe_agent.rag.retriever import vectorStore
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from src.cafe_agent.agents.llms import llm
from src.cafe_agent.prompts.rag import prompt_rag
from src.cafe_agent.rag.retriever import retriever

document_chain = create_stuff_documents_chain(llm, prompt_rag)

def busqueda_RAG(pregunta):

    related_docs = retriever.invoke(pregunta)

    if not related_docs:
        return {
            "respuesta": "No lo sé",
            "citaciones": [],
            "found_docs": False
        }

    respuesta = document_chain.invoke({
        "input": pregunta,
        "context": related_docs
    })

    return {
        "respuesta": respuesta,
        "citaciones": related_docs,
        "found_docs": True
    }