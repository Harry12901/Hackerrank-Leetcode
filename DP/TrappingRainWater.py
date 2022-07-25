'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        
        vol = 0
        for i in range(1,(len(height)-1)):
            lmax = height[i]
            rmax = height[i]
            for j in range(0,i):
                lmax = max(lmax, height[j])
            for j in range(i+1, len(height)):
                rmax = max(rmax,height[j])
            vol += (min(lmax,rmax)-height[i])
            
        return vol
