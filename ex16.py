from sys import argv
script, filename = argv

print(f"We are going to erase {filename}")
print(f"If you don't want that,hit CRTL_C (^C)")
print(f"If you want do that ,hit RETURN")

input(">>> ?")

print("Opening the file...")
#给open命令传入w参数，表示写入，传入r表示读取
target = open (filename,'w')

print("Truncating the file ,Goodbye! ")
#target.truncate()在使用w参数时，会自动替换前文本，清空文件的命令就不必须

print("Now I'm going to ask you for three lines" )

line1 = input("line 1 :")
line2 = input("line 2 :")
line3 = input("line 3 :")

print("I'm going to write these to the file .")

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
#将一堆代码转换成一行
target.write(f"{line1}\n{line2}\n{line3}")

print("And finally,we close it")
target.close()
