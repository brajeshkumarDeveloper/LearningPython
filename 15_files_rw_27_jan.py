# # with open('user.txt','w') as file:
# with open('user.txt','a') as file:
#     file.write('this is my first text file using python\n')
#     file.write('this is my second text file using python\n')
#     file.write('i am from bhopal\n')
#     file.write('i am from Unarmoured\n')

with open('user.txt', 'r') as f:
    # content =f.read();
    content =f.readlines();
for line in content:
    print(f'welcome {line.rstrip()}')