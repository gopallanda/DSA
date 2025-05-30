from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def typeofVehicle(self):
      pass
    @abstractmethod
    def wheels(self):
      pass
    @abstractmethod
    def use(self):
        pass
    @abstractmethod
    def speed(self):
        pass
    
class Car(Vehicle):
    def typeofVehicle(self):
       print("CAR")
    def wheels(self):
        print("wheels:4")
    def use(self):
       print("Personal and public transport")
    def speed(self):
       print("Average Speed: 120km/h")
class MotorCycle(Vehicle):

    def typeofVehicle(self):
       print("MotorCycle")
    def wheels(self):
        print("wheels:2")
    def use(self):
       print("Personal and public transport")
    def speed(self):
       print("Average Speed: 60km/h")
class Truck(Vehicle):
    def typeofVehicle(self):
       print("Truck")
    def wheels(self):
        print("wheels:8")
    def use(self):
       print("Goods transport")
    def speed(self):
       print("Average Speed: 150km/h")
obj1=Car()
obj2=MotorCycle()
obj3=Truck()
obj1.typeofVehicle()
obj1.wheels()
obj1.use()
obj1.speed()
obj2.typeofVehicle()
obj2.wheels()
obj2.use() 
obj2.speed()
obj3.typeofVehicle()
obj3.wheels()
obj3.use()
obj3.speed()