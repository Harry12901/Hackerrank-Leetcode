'''
Given two strings, determine if they share a common substring. A substring may be as small as one character.
'''

#Without Dictionary
#Approch 1:
'''
def twoStrings(s1, s2):
    for i in s1:
        if i in s2:
            return "YES"
    return "NO"
'''
#Using sets and intersection
#Approch 2:
'''
def twoStrings(s1, s2):
    return 'YES' if set(s1) & set(s2) else 'NO'
'''
'''
def twoStrings(s1, s2):
  return 'YES' if set(s1).intersection(set(s2)) else 'NO'

'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    for i in s1:
        if i in s2:
            return "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
