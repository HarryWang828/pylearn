#\t表示水平制表符，生成八个空格
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm spilt\non a line"
backslash_cat = "I'm \\ a \\ cat."

fat_cat="""
I will do a list
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

print('\a BEL')#响铃符，发声
print('\b BS')#退格符
print('\f FF')#进纸符，换页
print('\n LF')#换行，最常用
print('\v VT')#回到本行开头并前往下一行？
