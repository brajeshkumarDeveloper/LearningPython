a=16
b=9
c=12
print(a)

def someting():

    a=3
    x=globals()['a']
    b=5
    globals()['a']=20
    print(a+b+x)

someting()
print("outside function:",a)