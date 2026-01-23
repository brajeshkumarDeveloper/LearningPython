# def department_info(newDepartment):
#     print(f'Department is {newDepartment}')

 # class is blueprint or a template for creating objects and it defines the stricture and behaviour of that objects.
 # Object is an instance of a class. with its own unique data and the ability to perform actions
class Employee:
    COMPANY='ABC private limited'
    # constructor
    def __init__(self,name,email,department,salary):
        print('Constructor called')
        self.name = name
        self.email = email
        self.department = department
        self.salary = salary

    #method

    def emp_info(self):
        print(f'Name is {self.name}')
        print(f'Email is {self.email}')
        print(f'Department is {self.department}')
        print(f'Salary is {self.salary}')

    def new_department(self, param):
        print(f'Department is {param}')


# def new_department(self,department):
#         print(f'Department is {department}')
# # Objects
# emp1 = Employee('raju','raju@gmail.com','sales',50000)
# emp2 = Employee('rahul','rahul@gmail.com','dev',80000)
# emp1.emp_info()
# emp2.emp_info()
# emp1.new_department("QA")
# print(emp1.COMPANY)