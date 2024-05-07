#1.
massiv = [['folder', 'coursework.doc', 'folder', 'pict.png', 'data.accdb'],
        ['icon.ico', 'script.js', 'index.html', 'style.css', 'prog.py'],
        ['my_song.mp3', 'anapa-2003.jpg', 'cs_1.6.exe', 'folder', 'cheat.txt'],
        ['notes.txt', 'main.py', 'work.pdf', 'cartoon.mp4', 'array.py'],
        ['project.psd', 'cycle.py', 'folder', 'cycle.js', 'turtle.py']]
print('Начальный список:', massiv)
for i in massiv:
    for item in i:
        if item == 'folder':
            i.remove('folder')
for i in massiv:
    for item in i:
        if item == 'data.accdb':
            i.remove('data.accdb')
            i.append('data.sql')
print('Без папок и с заменой data:', massiv)
for i in massiv:
    for item in i:
        if '.py' in item:
            print('Все файлы .py:', item)
for i in massiv:
    for item in i:
        if '.js' in item:
            print('Все файлы .js:', 'new_' + item)

#2.
word_numb = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
n = int(input("Введите число от 0 до 9:"))
if 0 <= n <= 9:
    for i in range(n + 1):
        print(word_numb[i])
else:
    print('Введите число <= 9')

#3.
bin_sy = ['11011111', '11011101', '11000111', '11011100', '11011110']
dec_sy = []
for bin_num in bin_sy:
    dec_num = int(bin_num, 2)
    dec_sy.append(dec_num)
    print("Двоичное число", bin_num, "в десятичной системе:", dec_num)
max_num = max(dec_sy)
min_num = min(dec_sy)
print("Максимальное число:", max_num)
print("Минимальное число:", min_num)

#4.
matrix =    [[-446, 281, -80],
            [456, 432, -122],
            [13, 'error', 8]]
for i, row in enumerate(matrix):
    for j, item in enumerate(row):
        if isinstance(item, str):
            item = len(item)
            print(matrix)
sum = 0
for row in matrix:
    for item in row:
        sum += item
        print('Сумма всех элементов:', sum)

#5.
a = int(input('Колличество строк:'))
b = int(input('Колличество столбцов:'))
matrix = []
for i in range (a):
    a = []
    for j in range(b):
        c = int(input(f"Значение элемента {i+1},{j+1}:"))
        a.append(c)
    matrix.append(a)
for a in matrix:
    print(a)
sum_diagonal = 0
for i in range(3):
    sum_diagonal += matrix[i][2-i]
print("Сумма чисел по диагонали справа налево:", sum_diagonal)
