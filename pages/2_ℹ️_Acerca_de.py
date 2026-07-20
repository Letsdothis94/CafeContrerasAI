import streamlit as st

st.title("Acerca del Proyecto")

st.markdown("""
## Café Contreras AI

Este proyecto fue desarrollado utilizando:

- LangGraph
- LangChain
- Google Gemini
- FAISS
- Streamlit

### Funcionalidades

- Respuestas mediante RAG
- Clasificación de solicitudes
- Apertura automática de tickets
- Base de conocimiento interna
            
### Ejemplos de preguntas:
- ¿Cuáles son los beneficios para empleados?
- Me gustaría pedir información sobre el servicio de catering para 200 personas.
- ¿Cuál es el protocolo que debe seguir el personal si ocurre un accidente con líquido hirviendo en la sucursal?
- ¿Cuáles son las opciones de leche vegetal que ofrecemos para preparar el Flat White?
- ¿Qué variedad de café de origen utilizamos en nuestras sucursales y cuáles son sus notas de cata?
- ¿Qué vestimenta o uniforme deben portar los baristas durante su turno?
""")