class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        d = {}

        for let in s:
            if let in d.keys():
                d[let] += 1
            else:
                d[let] = 1
        
        for let in t:
            if let in d.keys():
                d[let] -= 1
            else:
                return False
        
        for k in d.keys():
            if d[k] != 0: return False
        
        return True