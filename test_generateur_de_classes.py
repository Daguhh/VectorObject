#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 22:38:11 2020

@author: david
"""


    

def genclass(param):
    
    c=param
    class MyClass:
        def __init__(self, a, b):
            self.a=a
            self.b=b
            self.c = c
        
        def calc(self):
            return self.a+self.b
    return MyClass

TestClass = genclass(10)

test = TestClass(a=12,b=1)