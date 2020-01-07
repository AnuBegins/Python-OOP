#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 12:47:59 2018

@author: ArunRam
"""

class Products:
        def __init__(self, price, item_name, weight, brand, status = "for sale"):
            self.price = price
            self.item_name = item_name
            self.weight = weight
            self.brand = brand
            self.status = status
        
        
        def Sell(self):
            self.status = "sold"
            return self
        
        def AddTax(self, tax):
            self.price = self.price * (1 + tax)
            return self.price
        
        def returnItem(self, reason_for_return):
            if reason_for_return == "defective":
                self.status = reason_for_return
                self.price = 0
            if reason_for_return == "like_new":
                self.status = "for sale"
            if reason_for_return == "opened":
                self.status = "used"
                self.price = self.price * .80
            return self
        
        def displayInfo(self):
            print("Price:",self.price)
            print("Item Name:",self.item_name)
            print("Weight:",self.weight)
            print("Brand:",self.brand)
            print("Status:",self.status)
            print("\n ")

