# block of code which perform some task and run when it is called.
# can be reuse many time in our program which lessen our lines of codes.
# we can pass argument to the method

# print('*'*20)
# print('Welcome to User')
# print('Thank you for your time')
# print('*'*20)

# # Defining the function
# def greeting(user_name, age, *hobbies):
#     print('*' * 20)
#     print(f'Welcome to {user_name} and his age is {age}')
#     # print(f'Hobby is {hobbies}')
#     for hobby in hobbies:
#         print(f'Hobby are {hobby}')
#     print('Thank you for your time')
#     print('*' * 20)
#
# # Calling a function
# greeting('brajesh',29,'singing','wondering')
# greeting('john',23,'playing')
# greeting('babu rao',11,'cricket');

# # Defining the function
# def greeting(user_name, age=90 ):
#     print('*' * 20)
#     print(f'Welcome to {user_name} and his age is {age}')
#     print('Thank you for your time')
#     print('*' * 20)
#
# # Calling a function
# greeting('brajesh',29)
# greeting('john',23)
# greeting('babu rao');


# Defining the function
def greeting(name, **user_info):
    print('*' * 20)
    print(f'Welcome to {name}')
    for key, value in user_info.items():
        print(f'{key}: {value}')
    print('Thank you for your time')
    print('*' * 20)

# Calling a function
greeting('brajesh',age=18,city='indore',email='test@gmail.com')
greeting('john',city='bhopal')
greeting('babu rao');


# add two number
def addition(num1,num2):
    sum=num1+num2
    return sum;
print(addition(10,20))