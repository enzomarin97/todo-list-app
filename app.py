import streamlit as st

# Estado inicial de las tareas
if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

st.title("To-Do List")

# Añadir una nueva tarea
task = st.text_input("Añadir una tarea:")
if st.button("Añadir"):
    if task:
        st.session_state["tasks"].append(task)

# Mostrar las tareas
if st.session_state["tasks"]:
    st.write("### Tareas pendientes:")
    for i, t in enumerate(st.session_state["tasks"]):
        st.write(f"{i+1}. {t}")

# Opción para borrar todas las tareas
if st.button("Borrar todas"):
    st.session_state["tasks"] = []
