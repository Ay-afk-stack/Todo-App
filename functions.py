# Constant variables are in uppercase for modules.
FILEPATH = "todos.txt"

# Fetching datas from the todos.txt file in read only mode.
def get_todos(filepath = FILEPATH):
    """
    Read a text file and return the List of to-do items. """
    with open(filepath,'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# Writing datas in the todos.txt file in write only mode
def write_todos(todos_arg , filepath = FILEPATH):
    """ Write a todo-item list in the Todos.txt File. """
    with open(filepath,'w') as file_local:
        file_local.writelines(todos_arg)



""" __name__ is a abstract word for python that holds the value of the file being executed like if i run the program directly now!! it will show __main__ as it is the main file for this function but if i run the program from the cli.py by importing  then the value of name will be filename. """

if __name__ == '__main__':
    print("Hello World")
    print(get_todos())