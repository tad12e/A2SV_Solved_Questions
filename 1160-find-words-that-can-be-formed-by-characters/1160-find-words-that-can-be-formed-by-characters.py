from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        dct=Counter(chars)
        res=0


        for i in words:
            if Counter(i)<=dct:
                res=res+len(i)
        return res



        