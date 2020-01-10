my_name = 'Harry Wang '
my_age = 17  # Going on 18
my_height = 179  # cm
my_weight = 51  # kg
my_eyes = 'black'
my_teeth = 'white'
my_hair = 'black'

my_height_in_inches = my_height * 0.3937008
my_weight_in_lbs = my_weight * 2.2046226

print(f"Let's talk about {my_name}")
print(f"He's {my_height}cms tall")
print(f"He's {my_weight}kgs heavy")
print("He's", round(my_height_in_inches), "inches tall")
print("He's", round(my_weight_in_lbs), "lbs heavy")
print(f"He's got {my_eyes}eyes and {my_hair}hair")
print(f"His teeth are usually {my_teeth}depending on coffee")

# round 函数可以四舍五入，但貌似不可以与f连用？
total = my_age + my_height + my_weight
print(f"If I add {my_age},{my_height},and{my_weight} I get{total}")
