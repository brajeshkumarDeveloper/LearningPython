num1=1;
num2= int(input("Enter a specified number: "));
numbers_lists=[];
for i in range(num1,num2+1):
    result="";
    if i%3==0:
        result= result+"Fizz";
        if i%5==0:
            result= result+"Buzz";
    elif i%5==0:
        result= result+"Buzz";
    else:
        result= i;
    numbers_lists.append(result);


print(numbers_lists);

# newList=[];
# for number in numbers_lists:
#     if number%3==0:
#         newList.append('Fizz')
#         print(f'Number is Fizz: {number}');
#     elif number%5==0:
#         newList.append('Buzz')
#         print(f'Number is Buzz: {number}');
#     elif (number % 3 == 0) and (number % 5 == 0):
#         newList.append('FizzBuzz')
#         print(f'Number is FizzBuzz: {number}');
#     else:
#         newList.append(number)
#
# print(newList);

