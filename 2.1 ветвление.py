# Задание 1
time = str(input("Какое сейчас время суток?"))
if time == "Утро":
    print("Пора вставать")
elif time == "День":
    print("Пора учиться")
elif time == "Ночь":
    print("Пора спать")
else:
    print("Нет ответа")

# Задание 2
password1 = "qwerty123"
password2 = str(input("Ввести пароль"))
if password1 == password2:
    print("Пароль правильный")
else:
    print("Пароль не подходит")

# Задание 3
a = input("Отправиться сейчас?")
if a == "да":
    b = input("Все ли припасы погруженны в лодку?")
    if b == "да":
        print("В путь!")
    else:
        print("Стоит подготовиться лучше")
else:
    print("Скажи как будешь готов")

# Задание 4
num1 = int(input("Введите первое число"))
num2 = int(input("Введите второе число"))
a = input("Что сделать с этими числами?: умножить, разделить, сложить, вычесть")
if a == "умножить":
    print(num1*num2)
elif a == "разделить":
    print(num1//num2)
elif a == "сложить":
    print(num1+num2)
elif a == "вычесть":
    print(num1-num2)
else:
    print("Нет ответа")

# Задание 5
squares = {
    "B1": "blue",
    "B2": "green",
    "B3": "blue",
    "B4": "green",
    "B5": None,
    "B6": "green",
    "B7": "blue",
    "B8": "green",
    "C1": "blue",
    "C2": "green",
    "C3": None,
    "C4": "blue",
    "C5": "blue",
    "C6": "blue",
    "C7": "green",
    "C8": "blue",
    "C9": "blue",
    "C10": "green",
    "C11": "green",
    "C12": None,
}
square = input("Введите номер квадрата (например, B1): ")
if square in squares:
    if squares[square] == "green":
        print("В квадрате", square, "сидит зеленый попугай.")
    elif squares[square] == "blue":
        print("В квадрате", square, "сидит синий попугай.")
    else:
        print("В квадрате", square, "никто не сидит.")
else:
    print("Ошибка: такого квадрата нет.")

# Задание 6
n = int(input("Введите число n"))
k = int(input("Введите число k"))
if n%k == 0 or k%n == 0:
    print("Кратно")
else:
    print("Не кратно")
