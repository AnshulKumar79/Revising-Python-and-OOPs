
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property  #decorator making email method as a property to call it as an attribute
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter  #making fullname method as an attribute setter to receive name as string and set  the first and last name of the instance

    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter  #making the fullname attribute as deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')
emp_1.fullname = "Corey Schafer"  #calling the setter

print(emp_1.first)
print(emp_1.email)  #calling email as an attribute
print(emp_1.fullname)  #calling fullname as an attribute

del emp_1.fullname  #calling the deleter


