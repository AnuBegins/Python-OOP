#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 14:51:01 2018

@author: ArunRam
"""


#class Parent:
  # parent methods and attributes here
#class Child(Parent): #inherits from Parent class so we define Parent as the first parameter
  # parent methods and attributes are implicitly inherited
  # child methods and attributes


# file vehicles.py
class Vehicle:
    def __init__(self, wheels, capacity, make, model):
        self.wheels = wheels
        self.capacity = capacity
        self.make = make
        self.model = model
        self.mileage = 0
    def drive(self,miles):
        self.mileage += miles
        return self
    def reverse(self,miles):
        self.mileage -= miles
        return self
class Bike(Vehicle):
    def vehicle_type(self):
        return "Bike"
class Car(Vehicle):
    def set_wheels(self):
        self.wheels = 4
        return self
class Airplane(Vehicle):
    def fly(self, miles):
        self.mileage += miles
        return self
v = Vehicle(4,8,"dodge","minivan")
print(v.make)
b = Bike(2,1,"Schwinn","Paramount")
print(b.vehicle_type())
c = Car(8,5,"Toyota", "Matrix")
c.set_wheels()
print(c.wheels)
a = Airplane(22,853,"Airbus","A380")
a.fly(580)
print(a.mileage)
