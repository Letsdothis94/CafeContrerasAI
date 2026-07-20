from src.cafe_agent.graph.workflow import graph
import streamlit as st
from uuid import uuid4

st.set_page_config(
    page_title="Café Contreras AI",
    layout="centered"
)

st.title("☕ Café Contreras AI")
st.caption("Powered by LangGraph + LangChain + Gemini")
st.markdown("""
### ¡Bienvenido al asistente virtual de Café Contreras!

Estoy aquí para ayudarte con consultas relacionadas con nuestros servicios,
beneficios para empleados y solicitudes de información.

Puedes realizar preguntas como:

- ¿Cuáles son los beneficios para empleados?
- ¿Qué vestimenta o uniforme deben portar los baristas durante su turno?
- Me gustaría solicitar información sobre el servicio de catering para 200 personas.

Nuestro asistente utiliza inteligencia artificial con una base de conocimiento
interna para brindarte respuestas rápidas y precisas.
""")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid4())

config = {
    "configurable": {
        "thread_id": st.session_state.thread_id
    }
}

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything..."):



    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant"):
        
        with st.spinner("Pensando..."):

            result = graph.invoke(
                {"pregunta": prompt},
                config=config
            )

            # st.write("FULL RESULT:")
            # st.write(result)

            answer = result["respuesta"]

            st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )