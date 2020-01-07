#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 15:30:18 2018

@author: ArunRam
"""

class Animal:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def walk(self):
        self.health -= 1
        return self
    
    def run(self):
        self.health -= 5
        return self
    
    def displayHealth(self):
        print("Health is:", self.health)
    
class Dog(Animal):
    def __init__(self,name):
        super().__init__(self,name)
        self.health = 150
        
    def pet(self):
        self.health += 5
        return self
        
class Dragon(Animal):
    def __init__(self, name):
        super().__init__(self, name)
        self.health = 170
    def displayHealth(self):
        print("I am a Dragon")
    def fly(self):
        self.health -= 10
        return self


a = Animal("joe", 130)
a.walk().walk().walk().run().run().displayHealth()

d = Dog("Joe Villarta")
d.walk().walk().walk().run().run().pet().displayHealth()

puff = Dragon("Puff")
puff.fly().displayHealth()

#b = Animal("joe",130)
#b.pet().displayHealth()