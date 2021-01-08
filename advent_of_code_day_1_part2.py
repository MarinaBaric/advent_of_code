import os
import sys
from itertools import combinations 

#NumList = [1721,299,55,77,99,675,1456,366,44,675,44,3333,22,979,55,445]
#test_list = [1721,299,55,77,99,675,1456,366,44,675,44,3333,22,979,55,445] 

sum = 2020

NumList = open('elements.txt').read().splitlines()
for i in range(len(NumList)):
    NumList[i] = int(NumList[i])

'''
sum of of three entries in list python
https://www.w3resource.com/python-exercises/challenges/1/python-challenges-1-exercise-9.php
https://www.geeksforgeeks.org/python-three-element-sum-in-list/
'''





def control_sum(mylist):
    for i in range(0, len(mylist)-2):
        for j in range(i+1, len(mylist)-1):
            for k in range(j+1, len(mylist)):
                if mylist[i] + mylist[j] + mylist[k] == sum:
                   mynewlist = []
                   mynewlist.append(mylist[i])
                   mynewlist.append(mylist[j])
                   mynewlist.append(mylist[k])
                   print("Summation of three elementts is : ", mynewlist)
                   print("Product of the three elements is : ",(mynewlist[0] * mynewlist[1] * mynewlist[2]))
    return control_sum
    
    
control_sum(NumList)

 