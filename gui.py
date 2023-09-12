import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),
                      key="todos",
                      enable_events=True,
                      size=(45,10))
edit_button = sg.Button("Edit")


window = sg.Window("My To-Do App",
                   layout=[[label,input_box,add_button],[list_box,edit_button]],
                   font=("Helvetica", 20))
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    #print(3, values["todos"])
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
                print(4, todo)
                new_todo = values["todo"].title()
                print(5, new_todo)
                todos = functions.get_todos()
                index = todos.index(todo)
                todos[index] = new_todo + "\n"
                functions.update_todos(todos)
                window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case sg.WINDOW_CLOSED:
            break
window.close()