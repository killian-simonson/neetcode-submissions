class Solution:
    def isPalindrome(self, s: str) -> bool:
        an = ""

        def getNext(an: str, L: bool):
            if len(an) < 1:
                return (an, False)
            
            if L:
                if len(an) == 1:
                    return (an, an[0])
                return (an[1:], an[0])
            else:
                return (an[:-1], an[-1])

        for l in s.lower():
            if l.isalnum():
                an = an + l
        
        print(an)
        
        while True:
            an, left = getNext(an, True)
            if not left:
                return True
            an, right = getNext(an, False)
            if not right:
                return False
            
            if left != right:
                return False
