import streamlit as st
import functions

todos = functions.get_todo()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"     ## session_state object contains the session detail and its a dictionary
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""

st.title("My To-Do App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

#### To create checkbox
# st.checkbox("Buy grocery")
# st.checkbox("Through the trash")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

# st.text_area("")
st.text_input(label="Enter a Todo", placeholder="Add new todo",
              on_change=add_todo, key="new_todo")     ## on_change argument is to connect this text box to an action or call-back function