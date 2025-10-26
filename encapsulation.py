class Student:
    def __init__(self, name, marks):
        self.__name = name      # private variable
        self.__marks = marks    # private variable

    # getter methods
    def get_name(self):
        return self.__name

    def get_marks(self):
        return self.__marks

    # setter methods
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks! Must be between 0 and 100.")

# object(instance) creation
s1 = Student("Anshul", 85)

# accessing private variables (through getters)
print(s1.get_name())   
print(s1.get_marks())

# trying to access directly
# print(s1.__marks)    #AttributeError

# updating using setter
s1.set_marks(92)
print(s1.get_marks())  #92

