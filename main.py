from database import log_in, create_table, add, select
from stmt import stmt_add, stmt_create, stmt_select

# create_table(stmt_create, is_commitable=True)
while True:
    print("Меню:")
    print("1. Регистрация")
    print("2. Вход в аккаунт")
    print("3. Выйти")

    choice = int(input("Выберите действие: "))

    if choice == 1:
        nickname = input("Введите никнейм: ")
        password = input("Введите пароль: ")
        add(stmt_add, (nickname, log_in(password)), is_commitable=True)
    elif choice == 2:
        nickname = input("Введите никнейм: ")
        password = input("Введите пароль: ")
        base = select(stmt_select, (nickname,), is_commitable=True)
        print(base)
        if len(base) == 0:
            print("Аккаунт не зарегистрирован!")
            break
        elif log_in(password) == base[0][1]:
            print("Вы успешно вошли в аккаунт!")
            base.clear()
            while True:
                print("Выберите действие: ")
                print("1. Поиск погоды по названию")
                print("2. Поиск погоды по координатам")
                print("3. Вывод истории поиска пользователя")
                print("4. Выйти")
                action = int(input("Выберите действие: "))
                if action == 1:
                    pass
                elif action == 2:
                    pass
                elif action == 3:
                    pass
                elif action == 4:
                    break
                else:
                    print("Неверный выбор. Пожалуйста, выберите снова.")
        else:
            print("Введен неправильный пароль!")
    elif choice == 3:
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите снова.")
