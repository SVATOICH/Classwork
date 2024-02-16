a = int(input("Введите кол-во чисел ряда Фибоначчи:"))
b1 = 0
b2 = 1
print(b1)
print(b2)
i = 2
while i < a:
    s = b1 + b2
    print(s)
    b1 = b2
    b2 = s
    i = i + 1
