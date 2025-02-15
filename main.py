while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip().lower()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ").strip().title() + "\n"

            with open('files/todos.txt', 'r') as f:
                todos = f.readlines()
            todos.append(todo)
            with open('files/todos.txt', 'w') as f:
                f.writelines(todos)

        case 'show':
            with open('files/todos.txt', 'r') as f:
                todos = f.readlines()
            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}. {item}"
                print(row)
        case 'edit':
            number = int(input("Number of todo to edit: "))
            number = number -1
            with open('files/todos.txt', 'r') as f:
                todos = f.readlines()
            existing_todo = todos[number]
            new_todo = input("Enter the new todo: ").strip()
            todos[number] = new_todo + '\n'
            with open('files/todos.txt', 'w') as f:
                f.writelines(todos)
        case 'complete':
            number = int(input("Number of todo to complete: "))
            with open('files/todos.txt', 'r') as f:
                todos = f.readlines()
            number = number - 1
            removed_todo = todos.pop(number).strip('\n')
            with open('files/todos.txt', 'w') as f:
                f.writelines(todos)
            message = f"Todo {removed_todo} was removed."
            print(message)

        case 'exit':
            break

print("Bye!")