# Time: O(n^2), Space: O(len(res))
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            # there is no need to check triplets which start from a positive number since the array is sorted and there is no way to get a sum of 0 from that.
            if nums[i] > 0:
                break
            # do not want to repeat triplets
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            # Idea: fix one number, solve 2 sum. This is another implementation of 2 sum, without hash map.
            target = -nums[i]
            l = i + 1
            r = n - 1
            while l < r:
                # > target, need to decrease the right pointer
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # do not want to repeat triplets i.e. if we have [-4, -1, -1, 0, 1, 2, 2], and we have just found [-1, -1, 2], we need to decrease our right pointer further, if not we end up with 2 still as our rightmost pointer, resulting in repetition. 
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res
