# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 22:58:25 2020

@author: ell
"""

import sys

if __name__ == "__main__":
    a, b = input().split(" ")
    
    if int(a)*int(b) % 2 == 0:
        print("Even")
    else:
        print("Odd")