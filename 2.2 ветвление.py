# 1
a = int(input("Введите количество минут"))
hour = a//60
minutes = a-hour*60
print(hour, "часа", minutes, "минут")

# 2
a = int(input("Введите рекомендованное количество часов сна"))
b = int(input("Введите максимальное количество часов сна"))
h = int(input("Введите количество часов сна"))
if h < a:
    print("Недосып")
elif h == a:
    print("Это нормально")
else:
    print("Пересып")

# 3
a = int(input("Введите а"))
b = int(input("Введите b"))
c = int(input("Введите с"))
p = (a+b+c)//2
s = (p*(p-a)*(p-b)*(p-c))**0.5
print(s)

# 4
a = input("Введите фигуру: треугольник, прямоугольник, круг,")
if a == "треугольник":
    a = int(input("Введите a"))
    b = int(input("Введите b"))
    c = int(input("Введите c"))
    p = (a+b+c)//2
    print(int(p*(p-a)*(p-b)*(p-c))**0.5)
elif a == "прямоугольник":
    a = int(input("Введите a"))
    b = int(input("Введите b"))
    print(a*b)
elif a == "круг":
    r = int(input("Введите r"))
    r1 = r**2
    print(3.14*r1)
else:
    print("Такой фигуры нет")

# 5
n = int(input("Введите количство программистов"))
if n % 10 in [2, 3, 4] and not n % 100 in [12, 13, 14]:
    print(n, "программиста")
elif n % 10 == 1 and n % 100 != 11:
    print(n, "программист")
elif n < 0:
    print("Отрицательного числа быть не может")
else:
    print(n, "программистов")

# 6
s = str(input())
sum1=int(s[0])+int(s[1])+int(s[2])
sum2=int(s[3])+int(s[4])+int(s[5])
if sum1==sum2:
  print('Счастливый')
else:
  print('Обычный')
