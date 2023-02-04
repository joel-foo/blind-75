# Time: O(n), Space: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # our left & right pointers are defined such that the area at the start has the maximum width. The only to maximise the area is to increase the height as the width decreases. This means always picking the left/right height which is greater.  
        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            max_area = max(max_area, min(height[l], height[r]) * (r - l))
            # this means the left height is limiting, so we should try to change the left height and see if we get a greater area. When the heights are equal, it does not matter which pointer we shift.(Why?)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_area

# Proof: Let Hl and Hr be the left and right heights, where Hl = Hr, with width (Hr - Hl).
# Suppose we choose to move Hl to the right, call the new height Hl'. Then there
# are 3 cases: 1. Hl' = Hr 2. Hl' < Hr 3. Hl > Hr. In all three cases, it is easy # to see that the new maximum area will always be lower than the original. 
# The same thing if we move Hr instead. We will not miss out any maximum area 
# larger than the current if we move either pointer. 
# It does not matter whether Hl or Hr is moved.  

