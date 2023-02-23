HELP = """
help - Напечатать справку по программе
add - Добавить задачу в список
show - Напечатать все добавленные задачи"""

tascs = []

command = input("Введите команду: ")
if command == "help":
    print(HELP)
elif command == "show":
    print(tascs)
elif command == "add":
    task = input("Введите название задачи: ")
    tascs.append(task)
    print("Задача добавлена")
else:
    print("Неизвестная команда")