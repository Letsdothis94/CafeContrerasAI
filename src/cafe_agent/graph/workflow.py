from langgraph.graph import START, END, StateGraph
from src.cafe_agent.graph.state import AgentState
from langgraph.checkpoint.memory import MemorySaver
from src.cafe_agent.graph.nodes import node_triaje, node_rag, node_open_ticket, node_final, node_pedir_info
from graph.routing import edge_triaje_decision

workflow = StateGraph(AgentState)
workflow.add_node("triaje", node_triaje)
workflow.add_node("RAG", node_rag)
workflow.add_node("ticket", node_open_ticket)
workflow.add_node("final_response", node_final)
workflow.add_node("pedir_info", node_pedir_info)

workflow.add_edge(START, "triaje")
workflow.add_conditional_edges("triaje", edge_triaje_decision, {
    "RAG": "RAG",
    "ticket": "ticket",
    "PEDIR_INFO": "pedir_info",
    "END": END
})

workflow.add_edge("RAG", "final_response")
workflow.add_edge("ticket", "final_response")
workflow.add_edge("final_response", END)

memory = MemorySaver()

graph = workflow.compile(
    checkpointer=memory
)