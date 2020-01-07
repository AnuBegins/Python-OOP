#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 12:05:32 2018

@author: ArunRam
"""

class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 15
        else:
            self.tax = 12
        self.display_all()
            
    def display_all(self):
        print("Price:",self.price)
        print("Speed:",self.speed,"mph")
        print("Fuel:",self.fuel)
        print("Mileage:",self.price,"mpg")
        print("Tax:",self.tax/100)
        print("\n ")
    
        return self

car1 = Car(2000,35,"Full",15)
car2 = Car(2000,5,"Not Full", 105)
car3 = Car(2000,15,"Kind of Full", 95)
car4 = Car(2000,25,"Full", 25)
car5 = Car(2000,45,"Empty", 25)
car6 = Car(2000,35,"Empty", 15)



