# Sum all values in a dictionary in Python

my_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
}

total = sum(my_dict.values())
print(total)  # 👉️ 6

# 👇️ [1, 2, 3]
print(list(my_dict.values()))