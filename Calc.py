def sum():
    a = 10
    b = 20
    print("Inside sum function", __name__)
    return print(a + b)

def main():
    sum()
    print("Calling from Calc function")

if __name__ == "__main__":
    main()


