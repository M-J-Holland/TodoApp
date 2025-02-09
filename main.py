todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip().lower()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ").strip()
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                print(f"{index + 1}. {item}")
        case 'edit':
            number = int(input("Number of todo to edit: "))
            number = number -1
            existing_todo = todos[number]
            new_todo = input("Enter the new todo: ").strip()
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of todo to complete: "))
            number = number - 1
            removed_todo = todos.pop(number)
            print(f"Removed todo: {removed_todo}")
        case 'exit':
            break

print("Bye!")