from functions import get_todos, update_todos
import time
# Create the todos list
todos = get_todos()

now = time.strftime("%b %d, %Y %H:%M:%S")

print("It is:",now)

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()
    if user_action.startswith("add") or user_action.startswith("new"):
        # ask for input
        if user_action == "add" or user_action == "new":
            todo = input("Enter a todo: ") + "\n"
        else:
            todo = user_action[4:].title() + "\n"
        # add the user's item into the list
        todos.append(todo)
        # open and rewrite the file
        update_todos(todos)
    elif user_action.startswith("show"):
        # listing all the todos
        for index, item in enumerate(todos):
            item = item.title().strip("\n")
            print("{}-{}".format(index + 1, item))
    elif user_action.startswith("edit"):
        try:
            if user_action == "edit":
                number = int(input("Number of the todo to edit: "))
            else:
                number = int(user_action[5:])
                if number not in range(1, len(todos)+1):
                    print(len(todos))
                    print("There is no such item with that number.")
                    continue
            # edit the task
            new_todo = input("Enter new todo: ")
            todos[number - 1] = new_todo + "\n"
            # update the file
            update_todos(todos)
        except (ValueError, IndexError):
            print("Your command is not valid.")
            continue
    elif user_action.startswith("complete"):
        try:
            if user_action == "complete":
                number = int(input("Number of the todo to complete: "))
            else:
                number = int(user_action[8:])
                if number not in range(1, len(todos) + 1):
                    print("There is no such item with that number.")
                    continue
            # remove the task
            removed_task = todos.pop(number - 1).strip("\n").title()
            # update the file
            update_todos(todos)
            print(f"Todo: {removed_task} was removed from the list")
        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")

print("Bye!")
