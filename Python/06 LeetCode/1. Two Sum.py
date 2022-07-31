# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.

# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.


# Follow-up: Can you come up with an algorithm that is less than O(n2)
# time complexity?


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            a = nums[i]
            for ii in range(i+1, len(nums)):
                b = nums[ii]
                if a + b == target:
                    return [i, ii]


# solution from comments
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        to check if any two element can sum up to target
        we can use greedy algorithm to iterate through the list

        record any needed(sum - element) and the index in a dict, 
        and check if any element appears in the dict
        if so, then we have the indexes

            time: O(N**2), memory: O(N)
        """

        need = {}

        for i, n in enumerate(nums):
            if n in need:
                return [need[n], i]
            need[target-n] = i


a = Solution
assert a.twoSum(a, [1, 7, 11, 2, 15], 9) == [1, 3]
assert a.twoSum(a, [3, 2, 4], 6) == [1, 2]
print('Done!')