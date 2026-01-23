active= True;
while active:
    first_number = int(input("enter the first number: "))
    next_number = int(input("enter the next number: "))

    listOfOperator = ["+", "-", "*", "/"]
    print('Select the operation: ')
    result = input('');
    output = first_number + next_number
    for operator in listOfOperator:
        if operator == result:
            print(f'Result of {first_number} {result} {next_number} is {output}')

    print(f'Continue the operation with {first_number + next_number}? y/n')
    my = input()
    if my == 'y':
        next_number = int(input("enter the next number: "))
        output1 = output + next_number
        print(f'Result of {output} {result} {next_number} is {output1}')

    else:
        active=False;
        





