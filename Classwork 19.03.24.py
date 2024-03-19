#1
x1 = float(input("Введите x1"))
y1 = float(input("Введите y1"))
x2 = float(input("Введите x2"))
y2 = float(input("Введите y2"))
x3 = float(input("Введите x3"))
y3 = float(input("Введите y3"))
print("Площадь треугольника:", ((x1 * y2 + x2 * y3 + x3 * y1) - (y1 + y2 + y3) * (x1 + x2 + x3) / 2) / 2)

#2
a = list(map(int, input("Введите 15 элементов массива через пробел: ").split())
z = [i for i in range(len(a)) if arr[i] == 0]print("Номера нулевых элементов массива:", z)
l = Nonefor i in range(len(arr)):
    if a[i] > 0:        l = i
print("Номер последнего положительного элемента в массиве:", l)

#3
a = list(map(int, input("Введите 17 элементов массива через пробел: ")
s = 0for b in a:
    if b < 0:        break
    sum_before_negative += bprint("Сумма всех элементов до первого отрицательного:", s)

#4
a1 = list(map(int, input("Введите 10 элементов первого массива через пробел: ")a2 = list(map(int, input("Введите 10 элементов второго массива через пробел: ")
if a1 == a2:    print("Массивы равны")
else:    print("Массивы не равны")
#5
a = list(map(int, input("Введите 20 элементов массива через пробел: ").z = [i for i in range(len(arr)) if a[i] == 0]
print("Одномерный массив из номеров нулевых элементов:", z)
