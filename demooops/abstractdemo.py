from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass
    @abstractmethod
    def brake(self):
        pass
    @abstractmethod
    def wheel(self):
        pass

class Car(Vehicle):
    color=None
    def drive(self):
        print("Hi im driving car and it is : ")
    def brake(self):
        print("Hi Car brake is perfet")
    def wheel(self):
        print("Hi Car has 4 wheels")

class Bike(Vehicle):
    color=None
    def drive(self):
        print("Hi im riding bike and it is : ")
    def brake(self):
        print("Hi Bike brake is disk and drum")
    def wheel(self):
        print("Hi Bike has 2 wheels")
