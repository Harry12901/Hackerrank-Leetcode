#MAXIMUM SUM PATH IN 2 ARRAYS
# You are given two sorted arrays of distinct integers nums1 and nums2.

# A valid path is defined as follows:

# Choose array nums1 or nums2 to traverse (from index-0).
# Traverse the current array from left to right.
# If you are reading any value that is present in nums1 and nums2 you are allowed to change your path to the other array. (Only one repeated value is considered in the valid path).
# The score is defined as the sum of uniques values in a valid path.

# Return the maximum score you can obtain of all possible valid paths. Since the answer may be too large, return it modulo 109 + 7.
class Solution:
    
    def maxSum(self, num1: List[int], num2: List[int]) -> int:
        M = 1000000007
        i=j = 0
        sum1=sum2=0
        res=0
        while(i<len(num1) and j<len(num2)):
            if(num1[i]<num2[j]):
                sum1+=num1[i]
                i+=1
            elif(num1[i]>num2[j]):
                sum2+=num2[j]
                j+=1
            else:
                res+= max(sum1,sum2)+num1[i]
                i+=1
                j+=1
                sum1=sum2=0
        
        while(i<len(num1)):
            sum1+=num1[i]
            i+=1
        while(j<len(num2)):
            sum2+=num2[j]
            j+=1
        res+=max(sum1,sum2)
        return res%M            
