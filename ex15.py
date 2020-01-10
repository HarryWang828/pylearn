# 调出argv库并赋值
from sys import argv

script, filename = argv
# 使用open命令打开文件，并赋给txt
txt = open(filename)
print(f"Here is your file,{filename}")
# 让txt执行read命令,显示文件内容
print(txt.read())
# 让用户继续输入文件
print('Type the filename again:')
file_again = input("> ")
# 打开input输入的文件
txt_again = open(file_again)
# 让txt执行read命令，显示文件内容
print(txt_again.read())
