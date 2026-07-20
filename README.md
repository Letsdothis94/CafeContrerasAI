# Café Contreras AI - Asistente Inteligente RAG

## Descripción

Este proyecto implementa un sistema inteligente para **Café Contreras** (México) que clasifica mensajes entrantes según su urgencia y tipo de flujo (`RAG`, `PEDIR_INFO`, `ABRIR_TICKET`). Cuenta con un módulo de Generación Aumentada por Recuperación (RAG) para responder consultas sobre manuales operativos, menús y políticas internas sin alucinaciones.

---

## Instalación

1. Clonar el repositorio

```bash
git clone https://github.com/Letsdothis94/CafeContrerasAI.git
cd CafeContrerasAI
```

2. Crear un entorno virtual

```bash
python -m venv venv
source venv/bin/activate
```

3. Instalar dependencias

```bash
pip install -r requirements.txt
```

4. Configurar la API Key

Crear un archivo `.env`

```env
GEMINI_API_KEY=TU_API_KEY
HF_TOKEN=TU_HUGGIN_FACE_KEY
```

5. Ejecutar la aplicación

```bash
streamlit run app.py
```

---

## Tecnologías Utilizadas

* **Framework:** LangChain
* **Modelo de Lenguaje:** gemini-3.1-flash-lite
* **Base de Datos Vectorial:** FAISS
* **Entorno:** Python 3.12+ & `python-dotenv`
* **UI:** Streamlit
* **Embedding:** gemini-embedding-001

---

## Ejemplo de Preguntas

**Pregunta:** ¿Cuáles son los beneficios para empleados?

**Respuesta:** En Café Contreras, los beneficios para nuestros empleados incluyen:

* Prestaciones de Ley Superiores: Alta inmediata ante el IMSS con el salario real, aportaciones al INFONAVIT, aguinaldo de 20 días y una prima vacacional del 35%.
* Consumo Interno Bonificado: Derecho a 2 bebidas de especialidad gratuitas durante la jornada laboral y un 40% de descuento en bolsas de grano entero y alimentos del menú.
* Fondo de Certificación SCA: Apoyo económico del 70% del costo para certificaciones oficiales de la Specialty Coffee Association (SCA) en los módulos de Barista Skills y Brewing, sujeto a una antigüedad mínima de 9 meses en la empresa.

---

## Deploying en Streamlit

<img width="1197" height="907" alt="deploy-streamlit" src="https://github.com/user-attachments/assets/57b8e0ce-eb8f-4614-8878-492ee463af9c" />

## Deploy Completed

<img width="1207" height="911" alt="deployed-streamlit" src="https://github.com/user-attachments/assets/f392befc-0e72-4682-a50f-0d70834ea3b3" />

## Autor

Cristian Contreras

## Website
[Visitar Café Contreras AI](https://cafecontrerasai.streamlit.app)
