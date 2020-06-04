
"""
Description:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.


0 <= nums.length <= 100
0 <= nums[i] <= 400

source: https://leetcode.com/problems/house-robber/
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        firstVal = nums[0] if len(nums) > 0 else 0
        firstResult = firstVal + self.rob(nums[2:])
        secondVal = nums[1] if len(nums) > 1 else 0
        secondResult = secondVal + self.rob(nums[3:])
        if firstResult > secondResult:
            return firstResult
        else:
            return secondResult
