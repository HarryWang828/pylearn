from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")
# 当文本无法读取时，使用encoding
in_file = open(from_file, encoding='utf-16 le')
indata = in_file.read()
# len显示文本大小，单位为字节
print(f"The input file is {len(indata)} bytes long")
print(f"Does the output file exist? {exists(to_file)}")

input("Ready,hit RETURN to continue,CTRL_C to exit")

out_file = open(to_file, 'w', encoding="utf-16 le")
out_file.write(indata)

print("Alright,all done")
# 调取文件后关闭十分重要，否则会占用大量资源
out_file.close()
in_file.close()
