#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:34:37 2020

@author: nick
"""

def maximum_subarray(array):
    # setting the maximum sub array
    max_sum = array[0]
    current_sum = max_sum
    for ele in array[1:]:
        current_sum = max(ele + current_sum, ele)
        max_sum = max(current_sum, max_sum)
    
    return max_sum
        
        s