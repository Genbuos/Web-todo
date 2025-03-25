import sqlite3


def connect_db():
    return sqlite3.connect('tasks.db')


def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            task TEXT NOT NULL,
            date_completed TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def add_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                   (username, password))
    conn.commit()
    conn.close()


def authenticate_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?',
                   (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None


def add_task(username, task):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (username, task) VALUES (?, ?)',
                       (username, task))
    conn.commit()
    conn.close()


def complete_task(task_id, date_completed):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET date_completed = ? WHERE id = ?',
                   (date_completed, task_id))
    conn.commit()
    conn.close()


def get_tasks(username):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, task FROM tasks WHERE username = ? AND date_completed IS NULL',
                   (username,))
    tasks = cursor.fetchall()
    conn.close()
    return tasks


def get_completed_tasks(username, date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT task FROM tasks WHERE username = ? AND date_completed = ? ',
                   (username, date))
    tasks = cursor.fetchall()
    conn.close()
    return tasks
