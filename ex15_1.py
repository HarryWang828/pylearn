#只用input来重写
filename=input("Please type what you want to search here \n>>>")
print(f"Here is your file,{filename}")
file = open(filename)
print(file.read())
