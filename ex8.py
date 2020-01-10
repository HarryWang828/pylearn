# 将四个{}赋值给formatter
formatter = "{} {} {} {}"
# 将1234传递给formatter
print(formatter.format(1, 2, 3, 4))
# 将one two three four传递给formatter
print(formatter.format("one", "two", "three", "four"))
# 同上，但是true/false不加引号是python关键字
print(formatter.format(True, False, False, True))
# 将formatter代表的四个{}传递给formatter，产生了16个{}
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    'Maybe a poem',
    'Or a song about fear '

))
