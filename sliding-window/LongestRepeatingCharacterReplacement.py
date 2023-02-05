# Time: O(n), Space: O(26) = O(1)
# Key idea: Keep track of the maximum frequency of the letters, check whether all other letters in the sliding window can be replaced with that most frequent letter in under k replacements. 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        maxCount = 0
        count = collections.Counter()
        l = 0
        for r, c in enumerate(s):
            count[c] += 1
            maxCount = max(maxCount, count[c])
            while (r - l + 1) - maxCount > k:
                count[s[l]] -= 1
                l += 1
            # move sliding window until valid, i.e. len(window) - maxCount = no. of letters that are not the most frequentone <= k replacements
            ans = max(ans, r - l + 1)
        return ans

# may use max(count.values()) instead of a maxCount that leads to higher time complexity -> O(26n) instead of O(n)
# Gotcha: maxCount works even though it doesn't have the "correct" values at all times. (Why?) The only way to increase len(window) is to increase maxCount. It does not matter if maxCount decreases as the left pointer moves. 
