from time import sleep

print('This is simple calculator!\n')
print("Choose action that you want to execute:\n"
      "Add: +\n"
      "Sub: -\n"
      "Mul: *\n"
      "Div: /\n"
      "Quit: q\n")


while True:  # Наш главный цикл
    while True:
        operation = input('Input operation -> ')  # Ввод операции с клавиатуры
        if operation not in ['+', '-', '/', '*', 'q']:  # Проверяем, существует ли введенная операция
            print('Such operation not exists, please try again!')  # Если нет, то просим ввести заново
        else:
            break
    if operation == 'q':  # Если ввели q, то вызодим из программы
        print('Well done! Bye)')
        sleep(3)
        break
    while True:  # ПРоверяем, является ли введенные символы числом
        try:
            first_num = int(input('Input first number -> '))
            break
        except ValueError:
            print("You didn't enter a number, please try again!")  # Если нет, то просим ввести еще раз
    while True:
        try:
            second_num = int(input('Input second number -> '))
            break
        except ValueError:
            print("You didn't enter a number, please try again!")
    # В зависимости от операции выполняем нужное действие
    if operation == '+':
        print(first_num + second_num)
    elif operation == '-':
        print(first_num - second_num)
    elif operation == '/':
        print(first_num / second_num)
    elif operation == '*':
        print(first_num * second_num)


