from src.cafe_agent.graph.workflow import graph
import streamlit as st

st.set_page_config(
    page_title="Café Contreras AI",
    page_icon="☕",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("☕ Café Contreras AI")

st.markdown("""
Bienvenido al asistente inteligente de **Café Contreras**.

Utiliza el menú lateral para navegar entre las diferentes secciones.

- 💬 Chat
- ℹ️ Acerca del proyecto
""")

with st.sidebar:
    st.markdown("""
    # ☕ Café Contreras
    
    ### Asistente IA
    
    Este asistente puede ayudarte con:
    
    ☕ Servicios  
    📚 Información interna  
    🎫 Solicitudes  
    🔎 Consultas empresariales
    """)