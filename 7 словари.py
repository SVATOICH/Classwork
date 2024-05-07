#1.
test_dict = {1: 'element 1', 2: 'element 2', 3: 'element 3', 4: 'element 4', 5: 'element 5'}
print(test_dict)
print(test_dict.keys())
print(test_dict.values())
print(test_dict.items())

#2.
test_dict = {'key 1': 'value 1', 'keyyy': 'vlaueee', '123': 123, 'random?': 'yes', 1: 'two'}
print(test_dict.get('keyyy'))
print(test_dict.get(1))

#3.
pc = {'info:': 'PC devices', 1: 'Video card', 2: 'Processor', 3: 'Monitor', 4: 'Strawberry', 5: 'Speakers'}
pc.pop(4)
pc.update({6: 'mouse'})
pc.update({7: 'headphones'})
pc.update({8: 'printer'})
print(pc)

#4.
double_sy = {1: '10111011', 2: '010101', 3: '11111101', 4: '110010', 5: '011010', 6: '100011001'}
double_sy = {'1': '10111011', '2': '010101', '3': '11111101', '4': '110010', '5': '011010', '6': '100011001'}
for key in double_sy.keys():
    num = int(input())
    
    print(f'Ключ: {key}')
#5.
books = {}
while True:
    book = input("Введите название книги:")
    if book == "всё" or "end":
        break
author = input("Ведите имя автора: ")
books[book] = author
print(books)
