'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = -inf
        sumi = 0
        for i in nums:
            sumi+=i
            maxi=max(maxi,sumi)
            if(sumi<=0): sumi=0
        return maxi
            
