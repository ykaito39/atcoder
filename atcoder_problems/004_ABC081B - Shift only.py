# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 21:10:35 2020

@author: ell
ABC081B - Shift only
"""


N = input()
A = input().split(" ")
A = [int(a) for a in A]

n = 0
flag = False
while(True):
    for a in A:
        if a%2 != 0:
            flag = True
    if flag == True:
        break
    
    A = [a/2 for a in A]
    n += 1

print(n)