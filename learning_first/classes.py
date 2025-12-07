# #define a class
# class Car:
#     pass # empty block

# my_car = Car()
# print(my_car)

# define a class with attributes and methods

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start_engine(self):
        print(f"The engine of the {self.make} {self.model} is starting.")

Mercedes = Car("Mercedes", "C-Class", 2022)

print(Mercedes.make)
print(Mercedes.model)       
print(Mercedes.year)

Mercedes.start_engine()



#inheritance example
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print(f"{self.name} is studying.")

class EngineeringStudent(Student):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def attend_lab(self):
        print(f"{self.name} is attending a lab session in {self.major}.")


class Vehicle:
    wheels = 4

    def __init__(self, brand, speed=0):
        self.brand = brand
        self.__speed = speed

    def drive(self, speed):
        self.__speed = speed
        print(f"{self.brand} is driving at {self.__speed} km/h")

    def __str__(self):
        return f"{self.brand} driving at {self.__speed} km/h"

class Car(Vehicle):
    def honk(self):
        print(f"{self.brand} goes beep beep!")

my_car = Car("Tesla")
my_car.drive(120)
my_car.honk()
print(my_car)
