#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 19:48:42 2018

@author: ArunRam
"""

#Objectives:
#Practice creating a class and creating new instances
#Practice chaining methods
#Practice writing flexible functions that can take a variable number of arguments
#HINT: To do this exercise, you will probably have to use 'return self'. If the method returns itself (an instance of itself), we can chain methods.
#
#Create a Python class called MathDojo that has the methods add and subtract. Have these 2 functions take at least 1 parameter.
#
#Then create a new instance called md to do the following task: md.add(2).add(2,5,1).subtract(3,2).result

class MathDojo:
        def __init__(self):
            self.result = 0
        
        def add(self, *args):            
            for val in args:
                self.result += val
            return self
            
        def subtract(self, *args):
            self.subtraction = 0
            
            for val in args:
                self.subtraction += val
                
            self.result -= self.subtraction
            return self


md = MathDojo()
a = md.add(2).add(2,5,1).subtract(3,2).result  #should perform 0+2+(2+5+1)-(3+2) and return 5. 

print(a)