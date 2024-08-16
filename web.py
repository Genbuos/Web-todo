import streamlit as st
import functions

todos = functions.read_file()


def add_todo():
    todo_n = st.session_state['new_todo'] + '\n'
    todos.append(todo_n)
    functions.write_file(todos)


todos = functions.read_file()

st.title("Todo.py")
st.subheader("Coded by - Jordan Mitchell")
st.write("Add a task to increase productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)

    if checkbox:
        todos.pop(index)
        functions.write_file(todos)
        del st.session_state[todo]
        st.rerun(scope='app')


st.text_input(label="", placeholder="Enter a task...", on_change=add_todo, key='new_todo')
