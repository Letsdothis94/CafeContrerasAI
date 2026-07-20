from typing import Literal, Dict, List
from pydantic import BaseModel, Field
from langchain_core.messages import SystemMessage, HumanMessage
from .llms import llm
from src.cafe_agent.prompts.triaje import SYSTEM_PROMPT

class TriajeOutput(BaseModel):
    decision: Literal["RAG", "PEDIR_INFO", "ABRIR_TICKET"]
    urgency: Literal["BAJA", "MEDIANA", "ALTA"]
    missing_fields: List[str] = Field(default_factory=list)


llm_triajeOutput = llm.with_structured_output(TriajeOutput)

def triaje(mensaje: str) -> Dict:
    output: TriajeOutput = llm_triajeOutput.invoke(
        [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=mensaje)
        ]
    )

    return output.model_dump()