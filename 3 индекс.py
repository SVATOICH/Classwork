# 1.
word = "программирование"
w1 = word[0] + word[1] + word[2] + word[3] + word[4] + word[5] + word[6] + word[7] + word[12]
print(w1)
w2 = word[3] + word[4] + word[5] + word[6] + word[7]
print(w2)
print(word[7:10])
print(word[9:12])
w5 = word[3] + word[4] + word[10] + word[6]
print(w5)

# 2.
w = str(input("Введите вашу строку"))
w1 = w[0]
print(w1)

# 3.
w = str(input("Введите вашу строку"))
w1 = w[1] + w[2] + w[3] + w[4]
print(w1)

# 4.
w = str(input("Введите вашу строку"))
b1 = w[0]
b2 = w[1]
print(b1 == b2)

# 5.
w = str(input("Введите вашу строку"))
w1 = w[::-1]
if w == w1:
    print("Это строка палиндромом")
else:
    print("Эта строка не является палиндромом")
