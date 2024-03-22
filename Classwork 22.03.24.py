#1.
a = input("Введите 1 число")
b = input("Введите 2 число")
if a < b:
    print(b, "больше", a)
elif a == b:
    print("Числа равны")
else:
    print(a, "больше", b)

#2.
a = int(input("Введите a"))
b = int(input("Введите b"))
c = int(input("Введите c"))
p = (a + b + c) / 2
s = (p*(p-a)*(p-b)*(p-c))
if s > 0:
    print("yes")
else:
    print("no")

#3.
a = int(input("Введите год"))
if a % 4 == 0:
    if a % 100 != 0 or a % 400 == 0:
        print("Високосный")
else:
    print("Не високосный")
