from collections import Counter
class Solution:
    
    def checkEqual(self, a, b) -> bool:
        #code here
        dct=Counter(a)
        dtc2=Counter(b)
        if len(a)!=len(b):
            return False
        return dct==dtc2
                
