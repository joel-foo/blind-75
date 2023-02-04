# Time: O(n), Space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dictionary with value as key and index in array as val
        dic = {}
        for i, num in enumerate(nums):
            # seen target - num previously (its index comes first)
            if target - num in dic:
                return dic[target - num], i
            dic[num] = i
