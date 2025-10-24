#polymorphism

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

    def showage(self):  #method-overriding
        print("your age is {}".format(self.age))

animal2= Human("Anshul", 20)
print(animal2.greet())
animal2.showage()



