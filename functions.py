FILEPATH = "todos.txt"


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


if __name__ == "__main__":
    print("Hello")
    print(read_file())
