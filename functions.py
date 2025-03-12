import json
import os
import datetime

FILEPATH = "todos.txt"
COMPLETED_TASKS_FILEPATH = "completed_tasks.txt"

def read_file(filepath=FILEPATH):
    """ This reads our txt file that stores the objectives added by the user.
        need a file object to persist usr input. the open method creates a file object
        with two arguments - fileName, access. readLines() is a method that returns a list of text
    """
    with open(filepath, 'r') as file_local:
        todo_local = file_local.readlines()
    return todo_local


def write_file(todo_arg, filepath=FILEPATH):
    """ This writes to our txt file storing the objectives added by the user.
       """
    with open(filepath, 'w') as file_local:
        todo_local = file_local.writelines(todo_arg)
    return todo_local

def read_completed_tasks(filepath=COMPLETED_TASKS_FILEPATH):
    if not os.path.exists(filepath):
        return {}
    completed_tasks = {}
    with open(filepath, 'r') as file_local:
        for line in file_local:
            date, task = line.strip().split('|', 1)
            if date not in completed_tasks:
                completed_tasks[date] = []
            completed_tasks[date].append(task)
    return completed_tasks

def write_completed_tasks(completed_tasks, filepath=COMPLETED_TASKS_FILEPATH):
    with open(filepath, 'w') as file_local:
        for date, tasks in completed_tasks.items():
            for task in tasks:
                file_local.write(f"{date}|{task}\n")

def calculate_streak(completed_tasks):
  streak = 0
  today = datetime.date.today().isoformat()
  for i in range(1, len(completed_tasks) + 1):
    day = (datetime.date.fromisoformat(today) - datetime.timedelta(days=i)).isoformat()
    if day in completed_tasks:
      streak += 1
    else:
      break
  return streak

if __name__ == "__main__":
    print("Hello")
    print(read_file())
