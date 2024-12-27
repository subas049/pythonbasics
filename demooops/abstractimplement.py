from abstractdemo import Car, Bike
from basics.assignmnt1 import *
car1=Car()
bike1=Bike()


def set_color(obj,color):
    obj.color=color

def get_color(obj):
    return obj.color

car1.brake()
car1.drive()
car1.wheel()

bike1.drive()
bike1.brake()

set_color(car1,'Red')
print(get_color(car1))
print(get_color(bike1))

printdetails()


