import streamlit as st

import database
import functions
import datetime

database.create_tables()


def register():
    st.sidebar.title("Register To Lock in!")
    username = st.sidebar.text_input("New Username")
    password = st.sidebar.text_input("New Password", type="password")
    if st.sidebar.button("Register To Lock in!"):
        database.add_user(username, password)
        st.sidebar.success("Welcome on the journey of improvement!")


def login():
    st.sidebar.title("Lock in!")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password", key='login_password')
    if st.sidebar.button("Lock in!", key='login_button'):
        with st.spinner("Authenticating..."):
            if database.authenticate_user(username, password):
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.sidebar.success("🔒")
            else:
                st.sidebar.error("Invalid username or password")


def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    if not st.session_state['logged_in']:
        register()
        login()
    else:
        todos = database.get_tasks(st.session_state['username'])

        def add_todo():
            todo_n = st.session_state['new_todo']
            database.add_task(st.session_state['username'], todo_n)
            st.session_state['new_todo'] = ''

        def update_completed_tasks(task_id):
            today = datetime.date.today().isoformat()
            database.complete_task(task_id, today)

            completed_tasks = database.get_completed_tasks(st.session_state['username'], today)
            streak = functions.calculate_streak(completed_tasks)
            st.session_state['streak'] = streak

        def display_completed_tasks():
            today = datetime.date.today().isoformat()
            tasks_today = database.get_completed_tasks(st.session_state['username'], today)
            st.write(f"Tasks Completed Today: {len(tasks_today)}")
            for task in tasks_today:
                st.write(f"- {task[0]}")

        st.title("Productivity Tracker")
        st.subheader("How often are you making plans and not following through? I was there too.")
        st.write("Add a task to increase productivity.")

        for task_id, todo in todos:
            checkbox = st.checkbox(todo, key=todo)

            if checkbox:
                update_completed_tasks(task_id)
                st.rerun(scope="app")
        st.text_input(label="", placeholder="Enter a task...", on_change=add_todo, key='new_todo')
        st.write(f"Current Streak: {st.session_state.get('streak', 0)} days")
        display_completed_tasks()  # Call the function to display completed tasks


if __name__ == "__main__":
    main()
