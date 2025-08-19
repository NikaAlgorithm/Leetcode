"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_table = {item: index for index, item in enumerate(nums)}
        for i in range(len(nums)):
            value = target - nums[i]
            if value in hash_table:
                return [i,hash_table[value]]
            
            
