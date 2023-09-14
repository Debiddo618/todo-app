import streamlit as st
import functions

# In terminal run -> streamlit run web.py

# Get the todos
todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo.title()+"\n")
    functions.update_todos(todos)
    st.session_state["new_todo"] = ""

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.update_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo: ",placeholder="Add a new todo...",on_change=add_todo, key="new_todo")

# uncomment to show session state in the web app
# st.session_state