import streamlit as st
import functions
import datetime

todos = functions.read_file()


def add_todo():
    todo_n = st.session_state['new_todo'] + '\n'
    todos.append(todo_n)
    functions.write_file(todos)
    st.session_state['new_todo'] = ''
    

def update_completed_tasks(completed_task):
    completed_tasks = functions.read_completed_tasks()
    today = datetime.date.today().isoformat()
    if today not in completed_tasks:
        completed_tasks[today] = []
    completed_tasks[today].append(completed_task)  # Append the completed task
    functions.write_completed_tasks(completed_tasks)

    streak = functions.calculate_streak(completed_tasks)
    st.session_state['streak'] = streak


def display_completed_tasks():
    completed_tasks = functions.read_completed_tasks()
    today = datetime.date.today().isoformat()
    tasks_today = completed_tasks.get(today, [])
    st.write(f"Tasks Completed Today: {len(tasks_today)}")
    for task in tasks_today:
        st.write(f"- {task}")
 

todos = functions.read_file()

st.title("Productivity Tracker")
st.subheader("How often are you making plans and not following through? I was there too.")
st.write("Add a task to increase productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)

    if checkbox:
        todos.pop(index)
        functions.write_file(todos)
        del st.session_state[todo]
        update_completed_tasks(todo.strip())
        st.rerun(scope='app')


st.text_input(label="", placeholder="Enter a task...", on_change=add_todo, key='new_todo')
st.write(f"Current Streak: {st.session_state.get('streak', 0)} days")

display_completed_tasks()  # Call the function to display completed tasks