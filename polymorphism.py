#Q1.Abstract class
    
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class car(Vehicle):
    def start(self):
        print ("car is starting...")

obj= car()
obj.start()




