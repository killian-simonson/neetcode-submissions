class Solution:

    def encode(self, strs: List[str]) -> str:
        fin = ""
        lens = [len(x) for x in strs]
        for (str, x) in zip(strs, lens):
            fin += f"{x}#{str}"
        
        return fin

    def decode(self, s: str) -> List[str]:
        lst = []
        while len(s):     # Works? IDK
            split1 = s.find("#")
            x = int(s[0:split1])
            split2 = split1 + x + 1
            lst.append(s[split1 + 1:split2])
            s = s[split2:]
        
        return lst

