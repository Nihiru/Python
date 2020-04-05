#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:29:53 2020

@author: nick
"""

def isHappy(number) -> bool:
    result = 0
    total = 0
    # implement a set that gets 
    happySet = set()
    while(number != 1):
        current_number = int(number)
        total = 0
        # code that divides the number into digits
        while(current_number != 0):
            rem = int(current_number %10)
            
            total += int(rem * rem)
            current_number  = int(current_number / 10)
            print(total)
        if(total in happySet):
           return False
       
        happySet.add(total)
        number = total
     
#            print(happySet)
    return True

print(isHappy(19))