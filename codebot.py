HELP = """
help - Напечатать справку по программе
add  - Добавить задачу в список
show - Напечатать все добавленные задачи"""

tascs = {

} # <--- это словарь

run = True

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
        if date in tascs:    # если дата есть в словаре, то добавляем зададчу в список
            task[date].append(tascs)
        else:
            # если даты нет в словаре, то добавляем задачу с ключем date
            if date in tascs:
                tascs[date] = []
                tascs[date].append(task)
            else:
                print("Такой даты не существует")
        print("Задача", task, "добавлена на дату", date)
    else:
        print("Неизвестная команда")
        break
print("До свидания!")