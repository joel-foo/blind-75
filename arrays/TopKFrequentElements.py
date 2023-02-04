# Naive Solution - Time: O(nlogn), Space: O(n), n = len(nums) 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        # dic with num as key, freq as value
        dic = Counter(nums)
        # sort the dic by their frequencies (values) in descending order
        for key, val in sorted(dic.items(), key = itemgetter(1), reverse = True):
            if k > 0:
                res.append(key)
                k -= 1
        return res



