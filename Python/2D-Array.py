# Given a  2D Array, :
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# An hourglass in  is a subset of values with indices falling in this pattern in 's graphical representation:
# a b c
#   d
# e f g
# There are 16 hourglasses in arr. 
# An hourglass sum is the sum of an hourglass' values. 
# Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum. The array will always be 6*6.

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
def cursum(arr,i,j):
    res = sum(arr[i][j:j+3])+arr[i+1][j+1]+sum(arr[i+2][j:j+3])
    return res
def hourglassSum(arr):
    res = -1000000007 
    for i in range(0,len(arr)-2):
        for j in range(0,len(arr)-2):
            res=max(res,cursum(arr,i,j))
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
