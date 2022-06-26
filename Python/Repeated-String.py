# There is a string, s, of lowercase English letters that is repeated infinitely many times. 
# Given an integer, n, find and print the number of letter a's in the first n letters of the infinite string.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    count = 0
    for i in s:
        if(i=='a'):
            count+=1
    count*=(n//len(s))
    r = n%len(s)
    if(r!=0):
        for i in range(0,r):
            print(i)
            if (s[i]=='a'):
                count+=1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
