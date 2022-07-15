'''
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each the array element between two given indices, inclusive. 
Once all operations have been performed, return the maximum value in the array.
'''

'''
Solution#1
--O(n*len(queries))--
def arrayManipulation(n, queries):
    arr = [0]*(n+1)
    print(arr)
    for q in queries:
        for i in range(q[0],q[1]+1):
            arr[i-1] += q[2]
    return max(arr)
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
import itertools
import math
def arrayManipulation(n, queries):
    arr = [0]*(n+1)
    for q in queries:
        arr[q[0]-1] += q[2]      
        arr[q[1]] -= q[2] 
        
    print(arr)
    
    s = 0
    m = -math.inf
    for i in arr:
        s+=i
        m = max(m,s)
    return m

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
