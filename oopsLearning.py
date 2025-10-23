#python_object_oriented_programming


class Employee:  #defining a class with name Employee

    def __init__(self, first, last, pay):  #defining constructor function for initialisation with arguments
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):  #defining a instance method(function) returning name of employee
        return '{} {}'.format(self.first, self.last)

#creating instances(objects) of class Employee passing the required parameters
emp_1 = Employee('Corey', 'Schafer', 50000)  
emp_2 = Employee('Test', 'Employee', 60000)