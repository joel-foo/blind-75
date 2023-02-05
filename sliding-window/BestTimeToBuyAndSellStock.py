# Time: O(n), Space: O(1)
# Use a greedy algorithm, we always keep any cost that is lower the current minimum, any higher costs we will maximise the difference.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        curr_min = prices[0]
        for p in prices:
            if p < curr_min:
                curr_min = p
            else:
                ans = max(ans, p - curr_min)
        return ans
