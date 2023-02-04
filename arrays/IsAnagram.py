# Time: O(len(s) + len(t)), Space:O(26) = O(1), only lowercase English letters
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # this guard is necesary because  without it, if len(s) < len(t), then e.g. s = "anag", t ="ana" returns True
        if len(s) != len(t):
            return False
        # Counter iterates over s and creates a dictionary with the characters as keys and their freq as values
        dic = Counter(s)
        for c in t:
            # if there are no available characters left/character doesn't exist in the first place
            if dic[c] == 0:
                return False
            dic[c] -= 1
        return True
