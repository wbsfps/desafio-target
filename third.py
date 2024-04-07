"""
3) Descubra a lógica e complete o próximo elemento:
"""

# a
list_ = []
for i in range(1, 14):
    if i % 2 != 0:
        list_.append(i)
print(list_)  # [1, 3, 5, 7, 9, 11, 13]

# b
list_ = [2, 4, 8, 16, 32, 64]
print(list_[-1] * 2)  # 128

# c
list_ = [0, 1, 4, 9, 16, 25, 36]
print(list_[-1] + 13)  # 49

# d
list_ = [4, 16, 36, 64]
print(9 ** 2)  # 81

list_ = [1, 1, 2, 3, 5, 8]
print(list_[-1] + list_[-2])  # 13

next_number = 200
list_ = [2, 10, 12, 16, 17, 18, 19, next_number]
