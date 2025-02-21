from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def move (self):
        pass
    @abstractmethod
    def drive(self):
        pass
class Car(vehicle):
    def __init__(self, speed):
        self.speed = speed
    def speed (self):
        return f"{self.speed} - has moved with high speed"
    def move(self):
        return f"{self.move} - has moved with high speed"
car1= Car("Audi")
print(car1)
car1.move()
print(car1)
car1.speed = 20
print(car1)