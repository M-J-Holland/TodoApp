while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip().lower()
    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"
        with open('files/todos.txt', 'r') as f:
            todos = f.readlines()
        todos.append(todo)
        with open('files/todos.txt', 'w') as f:
            f.writelines(todos)

    elif user_action.startswith('show'):
        with open('files/todos.txt', 'r') as f:
            todos = f.readlines()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            with open('files/todos.txt', 'r') as f:
                todos = f.readlines()
            existing_todo = todos[number]
            new_todo = input("Enter the new todo: ").strip()
            todos[number] = new_todo + '\n'
            with open('files/todos.txt', 'w') as f:
                f.writelines(todos)
        except (ValueError, IndexError):
            print("You have entered an invalid number. Please try again.")
            continue


    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            with open('files/todos.txt', 'r') as f:
                todos = f.readlines()
            number = int(number) - 1
            removed_todo = todos.pop(number).strip('\n')
            with open('files/todos.txt', 'w') as f:
                f.writelines(todos)
            message = f"Todo {removed_todo} was removed."
            print(message)
        except (ValueError, IndexError):
            print("You have entered an invalid number. Please try again.")
            continue


    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid.")

print("Bye!")
