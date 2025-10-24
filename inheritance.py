#inheritance

# class Factorymumbai:  #parent class or super class
#     a="I am an attribute mentioned inside factory"  #class attribute
#     def hello(self):  #instance method
#         print("hello I am a method inside factory")

# class Factorypune(Factorymumbai):  #child class or sub-class
#     pass

# obj= Factorymumbai()  #instance of parent class
# obj2= Factorypune()  #instance of child class
# obj2.hello()  #calling method defined inside the parent class


class Animal:
    def __init__(self,name):
        self.name=name
    
    def greet(self):
        return f"Hello, your name is {self.name}"

    def showage(self):
        pass

animal1= Animal("Giraffe")
print(animal1.greet())

class Human(Animal):
    def __init__(self, name, age):
        super().__init__(name)  #inheriting the __init__ functinality from the parent class
        self.age= age

    def showage(self):  #customizing the instance method defined in the parent class according to particular child class need
        print("your age is {}".format(self.age))

animal2= Human("Anshul", 20)
print(animal2.greet())
animal2.showage()
