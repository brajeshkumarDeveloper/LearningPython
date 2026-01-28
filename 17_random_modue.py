import random

#Generate a random float between 0 and 1

# print(random.random())
# print(random.randint(1,10))
# print(random.uniform(3.5,6.5))
#
# #Generate a random choice from a list
# fruits= ["apple", "banana", "cherry", "date"];
# ramdom_choice=random.choice(fruits)
# print(ramdom_choice)
# print(fruits)
# random.shuffle(fruits)
# print(fruits)

# //////////////////////////////////////////

# Dice program
while True:
    print(f'Number is {random.randint(1,6)}')
    user_input = input('Would you like to continue? (y/n)')
    if user_input == 'n':
        break;
