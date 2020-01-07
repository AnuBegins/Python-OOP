#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 19:40:06 2018

@author: ArunRam
"""

def varargs(arg1, *args):  # the '*' is the splat operator
    print("Got "+arg1+" and "+ ", ".join(args))
varargs("one") # output: "Got one and "
varargs("one", "two") # output: "Got one and two"
varargs("one", "two", "three") # output: "Got one and two, three"
