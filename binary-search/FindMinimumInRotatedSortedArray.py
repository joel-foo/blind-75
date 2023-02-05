# Time: O(logn), Space: O(1) 
# By rotating the array each time, we are taking the rightmost element (large elements) and putting it at the front. 
# Invariant: The array can be viewed in terms of 2 halves, and one half will always be sorted. If nums[l] <= nums[mid], the left part is sorted, then the current smallest is nums[l] and we minimise with nums[l]. Else right part is sorted and we minimise with nums[mid].  
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        ans = float('inf')
        while l <= r:
            mid = (l + r) // 2
            if nums[l] <= nums[mid]:
                ans = min(ans, nums[l])
                l = mid + 1
            else:
                ans = min(ans, nums[mid])
                r = mid - 1
        return ans
