# Type of Comprehension: Set Comprehension, set , list dictionary generator
# Description: This script demonstrates the use of
# set comprehension to create a set of squares of even

# list

menu= ["masala Chai", "coffee", "milk", "black tea", "green tea", "ginger tea"]

# for beverage in menu:
#     if "tea" in beverage:
#         print("I love " + beverage)
# [expression for item in iterable if condition]
black_tea= [my_tea for my_tea in menu if "tea" in my_tea]
print(black_tea)
