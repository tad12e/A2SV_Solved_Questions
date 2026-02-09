from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        sd=Counter(s)

        for key, value in sd.items():
            if value==1:
                return s.index(key)
        return -1

        