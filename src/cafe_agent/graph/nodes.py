from src.cafe_agent.graph.state import AgentState
from typing import Any
from src.cafe_agent.agents.triaje import triaje
from src.cafe_agent.rag.busqueda_rag import busqueda_RAG
from uuid import uuid4


def node_triaje(state: AgentState) -> dict[str, Any]:
    print("=== NODE_TRIAJE ===")

    return {
        "triaje": triaje(state["pregunta"])
    }

def node_rag(state:AgentState) -> dict[str, Any]:
    print("=== Node_RAG ===")

    response = busqueda_RAG(state['pregunta'])

    update: AgentState = {
        "respuesta": response['respuesta'],
        "citaciones": response['citaciones'],
        "rag_success": response['found_docs']
    }

    if response['found_docs']:
        update['final_action'] = "RAG"

        return update    

def node_open_ticket(state:AgentState) -> dict[str, Any]:
    print("=== Node_open_ticket ===")

    triaje_response = state['triaje']

    ticket = {
        "id": uuid4(),
        "status": "OPEN",
        "urgency": triaje_response['urgency'],
        "description": state['pregunta']
    }

    return {
        "ticket": ticket,
        "respuesta": (
            f"✅Hemos registrado correctamente tu solicitud.☕\n\n"
            f"**Número de ticket:** {ticket['id']}\n\n"
            f"**Prioridad:** {ticket['urgency']}\n"
            f"**Estado:** {ticket['status']}\n\n"
            "Nuestro equipo revisará tu caso y se pondrá en contacto contigo lo antes posible. "
            "Gracias por comunicarte con Café Contreras."
        ),
        "rag_success": False,
    } 

def node_final(state:AgentState):
    print("=== Node final ===")

    return {
            "respuesta": state.get("respuesta"),
            "citaciones": state.get("citaciones"),
            "ticket": state.get("ticket"),
            "rag_success": state.get("rag_success")
        }

def node_pedir_info(state: AgentState):

    campos = state["triaje"]["missing_fields"]

    return {
        "respuesta": (
            "Para poder ayudarte necesito un poco más de información.\n\n"
            "Por favor indícame:\n"
            + "\n".join(f"- {campo}" for campo in campos)
        ),
        "final_action": "PEDIR_INFO"
    }