# def代表define def开头后四格缩进的全是函数的内容
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses")
    print(f"You have {boxes_of_crackers} boxes_of_crackers")
    print(f"Man that's enough for a party")
    print(f"Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("Or,we can use variables from our script:")
amount_of_cheese = 20
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two,variable and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
