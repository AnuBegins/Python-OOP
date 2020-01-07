#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 12:28:06 2018

@author: ArunRam
"""

class Node:
    def __init__(self, value):  #constructor to initiate this object
        self.value = value  #stores a value
        self.next = None   # stores reference (to next item)
    
class SList:
    def __init__(self, value):
   #this approach automatically instantiates a head node object when 
   #the Single Linked List class object is instantiated     
        node = Node(value)  
        self.head = node  #head is an internal class variable that represents the beginning node
    
    def addNode(self, value):
        node = Node(value)
        runner = self.head
            
        while(runner.next != None):
            runner = runner.next
        runner.next = node
        
    def removeNode(self, val):  #remove node whose value = val
        runner = self.head
        print("runner initial:", id(runner))
        previous_node = None

        while runner != None:
            if runner.value == val:
                if previous_node != None:  # for nodes after head node
                    previous_node.next = runner.next
                    return
                else:
                    self.head = runner.next
                    return 
            # here's the 'traverse'
            previous_node = runner
            runner = runner.next
            print("previous:",id(previous_node), "runner:",id(runner))
        return 
     
    def printAllValues(self, msg=""):
        runner = self.head          # create a runner     
        print("\n\nhead points to ", id(self.head))
        print("Printing the values in the list ---", msg,"---")
        while(runner.next != None):
            print(id(runner), runner.value, id(runner.next))
            runner = runner.next        
        print(id(runner), runner.value, id(runner.next))
      
print("\n\n\n\n================== START OF THE PROGRAM ================")  
     
list = SList(5)
list.addNode(7)
list.addNode(9)
list.addNode(1)
#list.removeNode(9) # removes 9, which is one of the middle nodes in the list
#list.removeNode(5) # removes 5, which is the first value in the list
list.removeNode(1) # removes 1, which is the last node in the list
list.printAllValues("Attempt 1")