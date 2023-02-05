# Time: O(n), Space: O(128) = O(1)
# Idea: expand our window until we meet a invalid substring, maximising along the way. Invariant: if s[i..j] is invalid, then s[i..j+1],...., s[i...n-1] are invalid - we would not need to check any substrings thereafter.
# Shrink our window until we have a valid substring again. 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        count = collections.Counter()
        l = 0
        for r, c in enumerate(s):
            count[c] += 1
            while count[c] > 1:
                count[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
