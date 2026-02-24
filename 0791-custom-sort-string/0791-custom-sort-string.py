from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dect=Counter(s)

        out=""

        for i in range(len(order)):
            if order[i] in s:
                out+=order[i]*(dect[order[i]])
                print(i)

        dect2=Counter(out)
        for i in s:
            if i not in order:
                out+=i
                print(i)
        #out+=s[len(order)-1:]

        return out
        