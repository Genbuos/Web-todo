import json
import os
import datetime

FILEPATH = "todos.txt"
COMPLETED_TASKS_FILEPATH ="completed_tasks.json"

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
    try:
        with open(filepath, 'r') as file_local:
            return json.load(file_local)
    except json.JSONDecodeError:
        return {}

def write_completed_tasks(completed_tasks, filepath=COMPLETED_TASKS_FILEPATH):
    with open(filepath, 'w') as file_local:
        json.dump(completed_tasks, file_local)

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
