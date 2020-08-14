#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
count = 0
for i in range(0,n):
    for j in range(i,n):
        if(a[i]>a[j]):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
            count+=1
print("Array is sorted in "+str(count)+" swaps.")
print("First Element: "+str(a[0]))
print("Last Element: "+str(a[-1]))
