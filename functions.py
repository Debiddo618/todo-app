FILE_PATH = "files/todos.txt"


# Open and read the file, then return the todos
def get_todos(filename=FILE_PATH):
    with open(filename, "r") as file:
        # create a list of items
        todos_list = file.readlines()
    return todos_list


# takes in a todos and update the file
def update_todos(updated_todos, filename=FILE_PATH):
    with open(filename, "w") as todos_file:
        todos_file.writelines(updated_todos)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
