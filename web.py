import streamlit as st
import functions
import datetime

# Simple user database (for demonstration purposes)
USER_DB = {
    "user1": "password1",
    "user2": "password2"
}

def login():
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if username in USER_DB and USER_DB[username] == password:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.sidebar.success("Logged in successfully!")
        else:
            st.sidebar.error("Invalid username or password")

def main():
    if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
        login()
    else:
        todos = functions.read_file(st.session_state['username'])

        def add_todo():
            todo_n = st.session_state['new_todo'] + '\n'
            todos.append(todo_n)
            functions.write_file(todos, st.session_state['username'])
            st.session_state['new_todo'] = ''

        def update_completed_tasks(completed_task):
            completed_tasks = functions.read_completed_tasks(st.session_state['username'])
            today = datetime.date.today().isoformat()
            if today not in completed_tasks:
                completed_tasks[today] = []
            completed_tasks[today].append(completed_task)
            functions.write_completed_tasks(completed_tasks, st.session_state['username'])

            streak = functions.calculate_streak(completed_tasks)
            st.session_state['streak'] = streak

        def display_completed_tasks():
            completed_tasks = functions.read_completed_tasks(st.session_state['username'])
            today = datetime.date.today().isoformat()
            tasks_today = completed_tasks.get(today, [])
            st.write(f"Tasks Completed Today: {len(tasks_today)}")
            for task in tasks_today:
                st.write(f"- {task}")

        st.title("Productivity Tracker")
        st.subheader("How often are you making plans and not following through? I was there too.")
        st.write("Add a task to increase productivity.")

        for index, todo in enumerate(todos):
            checkbox = st.checkbox(todo, key=todo)

            if checkbox:
                todos.pop(index)
                functions.write_file(todos, st.session_state['username'])
                del st.session_state[todo]
                update_completed_tasks(todo.strip())
                st.rerun(scope='app')

        st.text_input(label="", placeholder="Enter a task...", on_change=add_todo, key='new_todo')
        st.write(f"Current Streak: {st.session_state.get('streak', 0)} days")

        display_completed_tasks()

if __name__ == "__main__":
    main()