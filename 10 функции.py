#1
def upper(t):
    text = ' '
    for i in t:
        if 'A' <= i <= 'Z':
            text += i
    return text

string = 'PriVet'
result = upper(string)
print(result)

#2
def punct(txt):
    z = '!?.,()'
    i = 0
    for j in txt:
        if j in z:
            i += 1
    return i

text = ('Привет...')

result = punct(text)
print(f'Знаки: {result}')

#3
def create_cube(x, y):
    if x <= 0 or y <= 0:
        return 'Числа должны быть положительными'
    cube = ''
    for i in range(y):
        row = '*' * x
        cube += row + '\n'
    return cube

x = 5
y = 5

cube = create_cube(x, y)
print(cube)

#4
def double(string):
    d_string = ''
    for i in string:
        d_string += i * 2
    return d_string

stroka = 'строка'

result = double(stroka)
print(result)

#5
def constructor(detals, figures, cars, trees):
    minimum = min(detals // 72, figures // 4, cars // 2, trees // 7)
    return minimum

detals = 144
figures = 8
cars = 4
trees = 14

result = constructor(detals, figures, cars, trees)
print(result)

#6
def create_list(kol, numbers = None):
    if numbers is None:
        return [0] * kol
    else:
        return numbers  

kol = 5
numbers = 3

result = create_list(kol, numbers)
print(result)
