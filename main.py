from database import log_in, create_table, add, select, find_coordinates, find_city
from stmt import stmt_cities, stmt_coordinates, stmt_main


# create_table(stmt_main["create"], is_commitable=True)
# create_table(stmt_cities["create"], is_commitable=True)
# create_table(stmt_coordinates["create"], is_commitable=True)
while True:
    print("Меню:")
    print("1. Регистрация")
    print("2. Вход в аккаунт")
    print("3. Выйти")

    choice = int(input("Выберите действие: "))

    if choice == 1:
        nickname = input("Введите никнейм: ")
        password = input("Введите пароль: ")
        add(stmt_main["add"], (nickname, log_in(password)), is_commitable=True)
        print("Вы зарегистрировались!")
    elif choice == 2:
        nickname = input("Введите никнейм: ")
        password = input("Введите пароль: ")
        base = select(stmt_main["select"], (nickname,), is_commitable=True)
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
                action = 'int(input("Выберите действие: "))'
                API_URL = "https://api.openweathermap.org/data/2.5/weather"
                API_KEY = "1e1a8269c08d2807448ce0a3d324e530"
                if action == 1:
                    city = input("Введите название города: ")
                    add(stmt_cities["add"], (nickname, city), is_commitable=True)
                    info = find_city(API_URL, city, API_KEY)
                    if info["cod"] != "404":
                        main = info["main"]
                        wind = info["wind"]
                        weather = info["weather"]
                        print(f"Погода - {weather[0]['main']}")
                        print(f"Температура: {main['temp'] - 273:.2f}")
                        print(f"Ощущается как {main['feels_like'] - 273:.2f}")
                        print(f"Влажность: {main['humidity']}%")
                        print(f"Давление: {main['pressure']}мм рт. ст.")
                        print(f"Скорость ветра: {wind['speed']} м/c")
                    else:
                        print("Город не найден!")
                elif action == 2:
                    lon = float(input("Введите долготу: "))
                    lat = float(input("Введите широту: "))
                    add(
                        stmt_coordinates["add"],
                        (nickname, lon, lat),
                        is_commitable=True,
                    )
                    info = find_coordinates(API_URL, lon, lat, API_KEY)
                    if info["cod"] != "404":
                        main = info["main"]
                        wind = info["wind"]
                        weather = info["weather"]
                        print(f"Погода - {weather[0]['main']}")
                        print(f"Температура: {main['temp'] - 273:.2f}")
                        print(f"Ощущается как {main['feels_like'] - 273:.2f}")
                        print(f"Влажность: {main['humidity']}%")
                        print(f"Давление: {main['pressure']}мм рт. ст.")
                        print(f"Скорость ветра: {wind['speed']} м/c")
                    else:
                        print("Координаты неправильные!")
                elif action == 3:
                    print("История поиска по названию города: ")
                    story = select(
                        stmt_cities["select"], (nickname,), is_commitable=True
                    )
                    for i in story:
                        print(i[1])
                    print("История поиска по координатам: ")
                    story = select(
                        stmt_coordinates["select"], (nickname,), is_commitable=True
                    )
                    for i in story:
                        print(f"{i[1]}, {i[2]}")
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
