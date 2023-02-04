# Attempt 1: Time: O(n), Space: O(?)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filtering/list comprehension will result in some extra overhead, so you can check for alphanumeric in the while loop instead.
        # s = ''.join(filter(str.isalnum, s)).lower()
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

# Attempt 2: Time: O(n), Space: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        s = s.lower()
        while l < r:
            # skip any non-alnum characters, we only want to compare alnum characters. 
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
