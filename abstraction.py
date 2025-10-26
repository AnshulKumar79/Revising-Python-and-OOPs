from abc import ABC, abstractmethod  #imported ABC and abstract_method from abc module
#abc is abstract base class

# Abstract class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

#subclass-1
class Car(Vehicle):
    def start(self):
        print("Car engine started.")

    def stop(self):
        print("Car engine stopped.")

# Another subclass-2
class Bike(Vehicle):
    def start(self):
        print("Bike started with a kick.")

    def stop(self):
        print("Bike stopped.")

# usage
v1 = Car()
v1.start()
v1.stop()

v2 = Bike()
v2.start()
v2.stop()

#error
'''v = Vehicle() can't instantiate abstract class'''
