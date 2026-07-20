from src.cafe_agent.graph.state import AgentState

def edge_triaje_decision(state: AgentState) -> str:
    print("=== edge_triaje_decision ===")

    triaje_response = state['triaje']

    if triaje_response['decision'] == "RAG":
        return "RAG"
    
    elif triaje_response['decision'] == "ABRIR_TICKET":
        return "ticket"
    
    elif triaje_response['decision'] == "PEDIR_INFO":
        return "PEDIR_INFO"
     
    else:
        return "END"