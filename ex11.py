print("How old are you?")
age = input()
print("How tall are you?")
height = input()
print("How much do you weight?")
weight = input()

print(f"So,you're {age} old, {height} tall and {weight} heavy")

# 字符串后加，end=''可以不换行,双引号也可以
print("How old are you?", end='')
age = input()
print("How tall are you?", end="")
height = input()
print("How much do you weight?", end='')
weight = input()

print(f"So,you're {age} old, {height} tall and {weight} heavy")
