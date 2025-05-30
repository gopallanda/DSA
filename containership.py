class Car:
    def display(self):
        print("i am contained class")
class bike:
    def __init__(self):
        self.car=Car()
    def display(self):
        self.car.display()
        print("i am a container class")
a=bike()
a.display()