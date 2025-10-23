class Employee:

    num_of_emps = 0 #class variable
    raise_amt = 1.04  #class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1 #everytime increment by 1 whenever init runs to count no. of employees

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):  #instance method for increasing the pay of instance(emp)
        self.pay = int(self.pay * self.raise_amt)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)
print(emp_2.fullname())

print(emp_1.__dict__)  #printing all the attributes of emp_1 instance
emp_1.raise_amt=1.05  #creating a separate instance variable and overwriting it with the given assignment to make it unique for emp_1 without altering the original value of class variable
print(emp_1.__dict__)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.raise_amt)  #1.04 from class var
print(emp_1.raise_amt)  #1.05 from instance var
print(emp_2.raise_amt)  #1.04 from corresponding class var
