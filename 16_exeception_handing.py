try:
    print(10 * 2)
    print(10 / 0)
except ZeroDivisionError:
    print('Kindly do not divide by zero')
    print(10 + 2)
    print(10 - 2)

# try:
#     with open('user.txt') as f:
#         content = f.readlines()
#         # print(content)
# except FileNotFoundError:
#     print('File not found')
#
# else:
#     for line in content:
#         print(f'Welcome {line.rstrip()}')

try:
    with open('user1.txt') as f:
        content = f.readlines()
        # print(content)
except Exception as e:
    print(e, type(e))

else:
    for line in content:
        print(f'Welcome {line.rstrip()}')
finally:
    print('Always execute finally')
    print('DB closed')