import functions
import PySimpleGUI as sg
import time

sg.theme("DarkTeal12")
clock = sg.Text('',key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),
                      key="todos",
                      enable_events=True,
                      size=(45,10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
layout = [[clock],[label,input_box,add_button],
          [list_box,edit_button,complete_button],
          [exit_button]]

window = sg.Window("My To-Do App",
                   layout=layout,
                   font=("Helvetica", 20))
while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            if values["todo"] != "":
                todos = functions.get_todos()
                todos.append(values["todo"].title() + "\n")
                functions.update_todos(todos)
                window["todos"].update(values=todos)
        case "Edit":
            if values["todos"] != [] and values["todo"] != "" and values["todo"] != values["todos"]:
                todo = values["todos"][0]
                new_todo = values["todo"].title()
                todos = functions.get_todos()
                index = todos.index(todo)
                todos[index] = new_todo + "\n"
                functions.update_todos(todos)
                window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case "Complete":
            todo = values["todo"]
            todos = functions.get_todos()
            if todo in todos or todo + "\n" in todos:
                if todo + "\n" in todos:
                    index = todos.index(todo+"\n")
                else:
                    index = todos.index(todo)
                todos.pop(index)
                functions.update_todos(todos)
                window["todos"].update(values=todos)
        case "Exit":
            break
        case sg.WINDOW_CLOSED:
            break
window.close()