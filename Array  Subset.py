#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        dc=Counter(a)
        dc1=Counter(b)
        if len(b)>len(a):
            return False
        for i in b:
            if i not in a or dc[i]<dc1[]:
                return False
        return True
    
    
    
    
