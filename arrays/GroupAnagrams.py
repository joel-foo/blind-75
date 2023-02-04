# Time: O(nklogk), Space: O(nk), where n = len(strs), k = max(len(strs[i]))
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        # the key would be the sorted string i.e. for "bat", "tab", "abt", all would share the same key "atb"
        for s in strs:
            key = ''.join(sorted(s))
            res[key].append(s)
        return res.values()
