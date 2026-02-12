import collections

class Solution:
    def findOriginalArray(self, changed):
        c = collections.Counter(changed)
        if c[0] % 2 != 0:
            return []

        original = []

        for x in sorted(c):
            if c[x] > c[2 * x]:
                return []
            if x == 0:
                # For zeros, need pairs
                pairs = c[x] // 2
                original.extend([0] * pairs)
                c[x] = 0
            else:
                count = c[x]
                original.extend([x] * count)
                c[2 * x] -= count
                c[x] = 0

        return original

    