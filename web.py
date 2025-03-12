import streamlit as st
import functions
import datetime

todos = functions.read_file()


def add_todo():
    todo_n = st.session_state['new_todo'] + '\n'
    todos.append(todo_n)
    functions.write_file(todos)
    st.session_state['new_todo'] = ''

def update_completed_tasks():
      #TODO make read_completed_tasks, write_completed_tasks in functtions.py
    completed_tasks = functions.read_completed_tasks()
    today = datetime.date.today().isoformat()
    if today not in completed_tasks:
        completed_tasks[today] = 0
    completed_tasks[today] += 1
    functions.write_completed_tasks(completed_tasks)

    streak = functions.calculate_streak(completed_tasks)
    st.session_state['streak'] = streak


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
        update_completed_tasks()
        st.rerun(scope='app')


st.text_input(label="", placeholder="Enter a task...", on_change=add_todo, key='new_todo')
st.write(f"Current Streak: {st.session_state.get('streak', 0)} days")