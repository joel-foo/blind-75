# Time: O(n), Space: O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        # multiply by numbers to the left
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]
        # multiply by numbers to the right.
        # We can create another array, using more space, or we can just use a suffix variable.
        suffix = 1
        # note that enumerate returns a generator, need to conver to to list first before calling reversed.
        for i, num in reversed(list(enumerate(nums))):
            ans[i] *= suffix
            suffix *= num
        return ans
