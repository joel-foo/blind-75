class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = collections.Counter(t)
        leftAns = -1
        min_len = len(s)
        required = len(t)
        l = 0
        # for characters Ci in t, count[Ci] >= 1, so as we go through S, we deduct the count, if the count is >= 0, we know we have used a character in t. 
        for r, c in enumerate(s):
            count[c] -= 1
            if count[c] >= 0:
                required -= 1
            #expand window until valid, shrink until invalid window, minimising len along the way. 
            while required == 0:
                if (r - l + 1) <= min_len:
                    min_len = r - l + 1
                    leftAns = l
                count[s[l]] += 1
                # characters in s that not in t will never be > 0, will be at most 0.
                if count[s[l]] > 0:
                    required += 1
                l += 1
        return "" if leftAns == -1 else s[leftAns: leftAns + min_len]
            
                
