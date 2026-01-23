# For Loop
# Execute a block of code for each item in the sequence (such as list,tuple,string, or range)

for i in 1,2,3,4,5:
    print(i);

mum=[1,2,3,4,5]
for i in mum:
    print(i);


user_list=['brajesh','john','jane'];
for user in user_list:
    print(user);

age_info={'raju':25, 'sham':40}

for key,value in age_info.items():
    print(f'Age of " {key}  is {value}')

for name in age_info.keys():
    print(f'Age of " {name} is {age_info[name]}')
for age in age_info.values():
 print(f'Age of " {age} is {age}')


for number in range(1,101):
    print(number);