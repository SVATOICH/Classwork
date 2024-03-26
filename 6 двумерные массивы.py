#1.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("matrix:")
for item in matrix:
    print(item)
print("нечётные числа matrix")
for item in matrix:
    for num in item:
        if num % 2 == 1:
            print(num)
count = 0
for item in matrix:
    for num in item:
        if num % 2 == 0:
            count += 1
print("кол-во чётных:", count)

#2.
matrix_1 = [[2, 4, 3, 6], [5, 7, 1, 5]]
matrix_2 = [[2, 9, 0, 2], [3, 4, 7, 6]]
answer_matrix = [[0, 0, 0, 0], [0, 0, 0, 0]]
for i1 in range(len(matrix_1)):
    for i2 in range(len(matrix_2[0])):
        answer_matrix = (matrix_1[i1][i2] * matrix_2[i1][i2])
        print(answer_matrix, end=' ')

#3.
fruits = [['Banana', 'apple'], ['apricot', 'Avocado'], ['lime', 'lemon'], ['Mango', 'grapes']]
for i in range(len(fruits)):
    for j in range(len(fruits[i])):
        if fruits[i][j][0].isupper():
            print(fruits[i][j])
#4.
random_elements = [['toy', 'bee', 'cheese', 'ear'],
                   [False, 'word', '0110110', 10],
                   ['happiness', '(」°ロ°)」', 'luck', None],
                   ['car', '<- code ->', 4.7, True]]
for i in random_elements:
    for index, item in enumerate(i):
        if index % 2 == 1:
            print(item)

#5.
x = int(input('Введите количество строк:'))
y = int(input('Введите количество столбцов:'))
matrix = []
for i in range(x):
    spisok = []
    for j in range(y):
        element = int(input(f"Введите значение элемента [{i}, {j}]:"))
        spisok.append(element)
    matrix.append(spisok)
print('Ваш двумерный массив:')
for x in matrix:
    print(x)
