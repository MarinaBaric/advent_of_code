import os
import sys

#NumList = [1721,979,366,299,675,1456]

#a = input("Enter elements: ").split()
#for i in range(len(a)):
#    a[i] = int(a[i])
#print(a)

NumList = open('elements.txt').read().splitlines()
for i in range(len(NumList)):
    NumList[i] = int(NumList[i])
#print(a)


def control_sum(mylist):
    x=0
    new_list = [i+mylist[x] for i in mylist]
    if 2020 in new_list:
        print(mylist[x],"+",mylist[new_list.index(2020)],"=",mylist[x]+mylist[new_list.index(2020)])
        print(mylist[x],"*",mylist[new_list.index(2020)],"=",mylist[x]*mylist[new_list.index(2020)])
    else:
        x = x+1
        print("bajs")
        control_sum(mylist[x:])
    return control_sum

control_sum(NumList)















