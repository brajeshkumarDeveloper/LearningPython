from array import *
from numpy import *

# arr=array( [10, 20, 30, 40, 50])
# print("Original array:", arr)
# for num in arr:
#     print(num)
# //////////////////////////////////////////////////////////////////

# arr = array( [1, 2, 3, 4, 5,7.6], int)
# print("Original array:", arr)
# print("Original array:", arr.dtype)

arr2= linspace(0,16,9)
# print("New array:", arr2)


arr3= arange(1,10,2)
# print("New array:", arr3)

arr4= logspace(1,40,5)
# print("New array:", arr4)
# print('%.2f'%arr4[4])

arr5 = zeros(5)
# print("New array:", arr5)

arr6 = ones(5, int)
# print("New array:", arr6)

# ====================================
arr1= array([6,2,3,4,5]) #-> shallow copy
arr2=arr1.copy() #-> deep copy
print(arr1)
print(arr2)


print(id(arr1))
print(id(arr2))

# print(max(arr1))
# arr2= array([1,8,7,4,5])
# arr3= arr1 + arr2
# arr4 = concatenate((arr1,arr2))
# print(arr4)
# print("Addition:", arr3)
# print("Original array:", arr)

