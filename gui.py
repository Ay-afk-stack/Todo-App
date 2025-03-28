import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values = functions.get_todos(), key='todos_key',enable_events=True, size = [45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

layout = [[label],[input_box,add_button],[list_box, edit_button,complete_button],[exit_button]]

window = sg.Window('My To-do App',layout,font = ('JetBrains Mono',12))

while True:
    # Destructing events and values from window.read()
    event, values = window.read()
    
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todos = values['todo']+'\n'
            todos.append(new_todos)
            functions.write_todos(todos)
            window['todos_key'].update(values=todos)
            
        case 'Edit':
            todo = values['todos_key'][0]
            new_todo = values['todo']+"\n"
            todos = functions.get_todos()
            index = todos.index(todo)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos_key'].update(values=todos)
            
        case 'Complete':
            todo_to_complete = values['todos_key'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos_key'].update(values = todos)
            window['todo'].update(value = "")
        
        case 'todos_key':
            window['todo'].update(value = values['todos_key'][0])
        
        case 'Exit':
            break
        
        case sg.WIN_CLOSED:
            break
print('Bye')
window.close()