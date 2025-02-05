todos = []

while True:
    user_action = input("Type add, show or exit: ").strip().lower()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ").strip()
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break

print("Bye!")