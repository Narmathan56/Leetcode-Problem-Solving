
# Problem: Add Two Numbers
# LeetCode: https://leetcode.com/Narmathan26 
# Solved by Narmathan


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}

        for i, num in enumerate(nums):
            need=target-num


            if need in seen:
               return seen[need],i

            seen[num]=i       
