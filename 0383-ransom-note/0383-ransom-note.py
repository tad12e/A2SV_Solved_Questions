from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dect1=Counter(ransomNote)
        dect2=Counter(magazine)

        return dect1<=dect2