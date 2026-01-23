

# print('Enter a no. to check if that is Even or not')
#
# user_input="";
#
# while user_input != 'q':
#     user_input = input('Enter a no. or q for quit: ')
#     if user_input.isdigit():
#         if int(user_input) % 2 == 0:
#             print('Even')
#         else:
#             print('Odd')

# while True:
#     num=int(input('Enter a no. : '))
# =================================================

# count the program

# count =1;
# while count <= 5:
#     print(count)
#     count += 1;
#
# msg='';
# while msg != 'quit':
#     msg=input('Enter our message: ')
#     print(msg)
#
# active=True;
# while active:
#     msg=input('Enter our message: ')
#     if msg == 'exit':
#         active=False;

# =======================================
num=[1,29,20,29,40,50,29];

while 29 in num:
    num.remove(29);
print(num)

for n in num:
    if n==40:
        break;
    print(n)

for n in num:
    if n==40:
        continue;
    print(n)