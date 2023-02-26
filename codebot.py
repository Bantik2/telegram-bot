HELP = """
help - Напечатать справку по программе
add  - Добавить задачу в список
show - Напечатать все добавленные задачи
random - Добавляет случайную задачу на дату сегодня"""

RANDOM_TASK = "Купить порошок для стирки"

tascs = {

} # <--- это словарь

run = True

def add_todo(date, task):
    if date in tascs:    # если дата есть в словаре, то добавляем зададчу в список
            tascs[date].append(task)
    else:
        tascs[date] = []
        tascs[date].append(task)
    print("Задача", task, "добавлена на дату", date)

while run:
    # Цикл выполняется пока не будет введена команда, которой нет в HELP
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("Введите дату для отображения списка задач: ")
        if date in tascs:
            for task in tascs[date]:
                print('- ', task)
        else:
            print("Такой даты нет")
    elif command == "add":
        date = input("Введите дату для добавления задач: ")
        task = input("Введите название задачи: ")
        add_todo(date, task)
    elif command == "random":
        add_todo("сегодня", RANDOM_TASK)
    else:
        print("Неизвестная команда")
        break
print("До свидания!")