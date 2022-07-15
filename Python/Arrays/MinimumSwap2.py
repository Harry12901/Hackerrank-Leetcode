'''
You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. 
You are allowed to swap any two elements. Find the minimum number of swaps required to sort the array in ascending order.
'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.

def minimumSwaps(arr):
    a = {}
    for index,val in enumerate(arr):
        a[val] = index
        
    print(arr)
    print("index",a)
    count =0
    for i in range(len(arr)):
        if arr[i]!=i+1:
            #alt: time(O(n^2))
            #t = i+1
            # while arr[t]!=i+1:
            #     t+=1
            #swap arr[i] and arr[t]
            
            temp = arr[i]
            arr[a[i+1]]= arr[i]
            arr[i]= i+1
            
            a[temp]=a[i+1]
            a[i+1] = i

            count+=1
        
    print(arr)        
            
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
