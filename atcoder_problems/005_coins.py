# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 00:26:06 2020

@author: ell
005ABC087B - Coins
"""


coins_500 = input()
coins_100 = input()
coins_50 = input()
sum_result = input() #50の倍数 0, 50, 100, 150, ... 
sum_result = int(sum_result)

how_many_ways = 0
result = 0
tmp = 0
for n_500 in range(1, int(coins_500)+1):
    for n_100 in range(1, int(coins_100)+1):
        for n_50 in range(1, int(coins_50)+1):
            result += 50
            #print(result)
            if result == sum_result:
                how_many_ways += 1
                result = 0
                break
        
        result += 100
        #print(result)
        if result == sum_result:
            how_many_ways += 1
            result = 0
            break
            
    result += 500
    #print(result)
    if result == sum_result:
        how_many_ways += 1
        result = 0
        break

print(how_many_ways)