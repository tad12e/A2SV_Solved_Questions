class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        shortest = min(strs, key=len)
        prefix = ""

        for i in range(len(shortest)):
            ch = shortest[i]
            for word in strs:
                if word[i] != ch:
                    return prefix
            prefix += ch

        return prefix
