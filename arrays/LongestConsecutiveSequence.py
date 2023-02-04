# Time: O(n), Space: O(n)

# naive solution would be to sort the array (O(nlogn)), and then find the maximum length of consecutive elements subarray. But need to solve in O(n) time / in O(n^2) where each element is incremented until it's not possible.

# We want to find where the consecutive seq starts, and count upwards. For e.g. if we have 2 and 3 in our array, it is sufficient to length of sequence starting with 2. The invariant of the problem is: if num and num-1 present in our array, then we only need to check seq. starting from num-1 since len(seq. starting from num-1) > len(seq. starting from num).

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
        s = set(nums)
        res = 0
        for num in s:
            # if num - 1 not in set, it is the start of a new seq
            if (num - 1) not in s:
                count = 0
                while num in s:
                    count += 1
                    num += 1
                res = max(res, count)
        return res
