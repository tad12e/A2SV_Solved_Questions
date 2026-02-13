from collections import Counter
class Solution:
    def findValidPair(self, s: str) -> str:
        dect=Counter(s)
        length=len(s)

        for i in range(length-1):
            if s[i]!=s[i+1] :
                if dect[s[i]]==int(s[i]) and dect[s[i+1]]==int(s[i+1]):
                    return s[i]+s[i+1]
        return ""


        