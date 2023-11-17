def display_todo_list(todo_list):
    if not todo_list:
        print("Ypur to-do list is empty.")
    else:
        print("To-Do List: ")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
def add_task(todo_list, task):
    todo_list.append(task)
    print(f"Task '{task}' added to the to-so list.")
def delete_task(todo_list, index):
    if 1 <= index <= len(todo_list):
        deleted_task = todo_list.pop(index - 1)
        print(f"Task '{deleted_task}' deleted from the to-do list.")
    else:
        print("Invalid index,Please enter a valid index.")
def to_do_list_manager():
    todo_list = []
    while True:
        print("\nTo-Do List Manager")
        print("1.Display to-do list")
        print("2.Add a task")
        print("3.Delete a task")
        print("4.Quit")
        choice = input("Enter your choice (1/2/3/4): ")  
        if choice == '1':
            display_todo_list(todo_list)
        elif choice == '2':
            task = input("Enter the list: ")
            add_task(todo_list,task)
        elif choice == '3':
            index = int(input("Enter the index of the task to delete: "))
            delete_task(todo_list,index)
        elif choice == '4':
            print("To-Do List Manager closed")
            break
        else:
            print("Invalid choice.Please enter 1,2,3,4")
to_do_list_manager()                                          