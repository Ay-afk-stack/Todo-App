# from functions import get_todos, write_todos
import functions
import time


now = time.strftime("%Y-%m-%d %H:%M:%S")
today_date , time_now = now.split(" ")
print(f"Today's Date: {today_date} and Current Time: {time_now}")
while True:
    # Get user input and strip space chars from it.
    user_action = input("Type add, show, edit, complete or exit:").strip()

    # Check User actions
    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]+'\n'

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        # List-comprehension
        # new_todos = [item.strip('\n') for item in todos]

        todos = functions.get_todos()

        if not todos:
            print("No Todos Found!")
        else:
            for index,todo in enumerate(todos):
                print(f"{index+1}. {todo.strip('\n')}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            index = number-1

            todos = functions.get_todos()

            todos[index] = input("Enter a new todo:")+"\n"

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid!")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            index = number-1

            todos = functions.get_todos()

            removed_todo=todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)

            message = f'Todo {removed_todo} was removed from the list'
            print(message)

        except IndexError:
            print("No Todo found with that number!")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Invalid command!")
print("Bye!")