class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack is None or needle is None or haystack == '' or needle == '' :
            return -1;
        strLen = len(haystack);
        subStrLen = len(needle);
        for i in range(strLen - subStrLen + 1) :
            if haystack[i:i+subStrLen] == needle :
                return i;
        return -1;