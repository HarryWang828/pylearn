#input("括号内为提示别人要输入的内容")
age = input("How old are you? ")
height =input("How tall are you? ")
weight = input("How much do you weight? ")

print(f"So,you're {age} old, {height} tall and {weight} heavy.")
#如果这么写，无法产生输入
print("How old are you?",input())
