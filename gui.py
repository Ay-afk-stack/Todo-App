import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window('My To-do App',[[label],[input_box,add_button]],font = ('Helvetica',20))

while True:
    # Destructing events and values from window.read()
    event, values = window.read()
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todos = values['todo']+'\n'
            todos.append(new_todos)
            functions.write_todos(todos)
            print(f"{values['todo']} added!")
        case sg.WIN_CLOSED:
            break

window.close()