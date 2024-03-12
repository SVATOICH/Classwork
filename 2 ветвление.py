# Задание 1
num1 = int(input("Введите первое число"))
num2 = int(input("Введите второе число"))
if num1 == 0 or num2 == 0:
    print("Не удается выполнить исчисление с 0")
elif num1 % 2 == 0 and num2 % 2 == 0:
    print("Сумма двух четных чисел равна:", num1 + num2)
elif num1 % 2 != 0 and num2 % 2 != 0:
    print("Произведение двух нечетных чисел равно:", num1 * num2)
else:
    larger_num = max(num1, num2)
    smaller_num = min(num1, num2)
    print("Разница между числами", larger_num, "и", smaller_num, "это", larger_num - smaller_num)

# Задание 2
num1 = int(input("Введите первое число :"))
num2 = int(input("Введите втоое число="))
if num1 > 0 and num2 < 0 :
    result = num1 + num2
    print(f"сумма двух полжительных чисел : {result}")
elif num1 < 0 or num2 < num2:
    result = num1 * num2
    print(f"произведение двух отрицательных чисел: {result}")
elif num1 == 0 or num2 == 0 :
        print("cannot perfom calculations with 0")
else:
        result = num1 - num2 
        print(f"Разница между двумя числами {result}")
        
# Доп задание
letter = int(input("Введите количество писем"))
if letter > 100:
    print("Сделать рассылку")
else:
    print("Не делать рассылку")
