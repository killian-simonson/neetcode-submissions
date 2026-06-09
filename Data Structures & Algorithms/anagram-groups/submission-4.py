class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for i, s in enumerate(strs):
            st = tuple(sorted(list(s)))
            if st not in d.keys():
                d[st] = [i]
            else: d[st].append(i)
        
        return [[strs[i] for i in value] for value in d.values()]
