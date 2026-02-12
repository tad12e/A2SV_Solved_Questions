from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cs = Counter(s)
        ct = Counter(t)

        steps = 0
        for c in cs:
            if cs[c] > ct[c]:
                steps += cs[c] - ct[c]

        return steps

