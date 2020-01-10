# *代表接受函数所有参数并放到args里，很少用
def print_two(*args):
    arg1: object
    arg1, arg2 = args
    print(f"arg1: {arg1} arg2: {arg2}")


# python中可以不解包函数,就像下面那样

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}  arg2: {arg2}")


def print_one(arg1):
    print(F"arg1: {arg1}")


def print_none():
    print("I got nothing")


print_two("Harry", "Wang")
print_two_again("Harry", "Wang")
print_one('First!')
print_none()
