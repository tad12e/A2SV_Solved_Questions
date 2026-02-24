class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        j=len(needle)
        for i in range(len(haystack)):
            if needle==haystack[i:j]:
                return i
            j+=1
        return -1
