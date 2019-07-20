#从系统中引入argv模块，即库
from sys import argv
#调用argv，并将其赋给四个值
script,first,second,third = argv

print("The script is called:",script)
print("Your first variable is:",first)
print("Your second variable is:",second)
print("Your third variable is:",third)
