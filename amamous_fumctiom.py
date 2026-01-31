#
# def square(a):
#     return print(a*a)
#
# square(5)
from functools import reduce

from db.db_connection_30_01 import result

# anomalous function

# t= lambda a,b : a+b
# r = t(5,6)
# print(r)

def is_even(n):
    return n % 2 == 0
is_even(9);
nums = [1,2,3,4,5,6,7,8,9,10]
evens= list(filter(lambda b:b%2==0, nums))
print(evens)
double_values=  list(map(lambda x: x*2, evens))
print(double_values)

sum = reduce(lambda x,y:x+y, evens)
print(sum)