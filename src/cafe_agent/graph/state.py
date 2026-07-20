from typing import TypedDict, Optional, Any, Literal, NotRequired

class Ticket(TypedDict):
    id: str
    status: Literal["OPEN", "IN_PROGRESS", "CLOSED"]
    urgency: Literal["BAJA", "MEDIANA", "ALTA"]
    description: str

class AgentState(TypedDict):
    pregunta: str
    triaje: Optional[dict]
    respuesta: Optional[str]
    citaciones: Optional[str]
    rag_success: bool
    final_action: Optional[str]
    ticket: NotRequired[Ticket]