
from collections import Counter
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        

        dect1=Counter(pattern)
        dect2=Counter(s.split())

        value1=[value for value in dect1.values()]
        value2=[value for value in dect2.values()]
        print(value1, value2)
        
        dect3=defaultdict(str)

        for i, j in zip(s.split(), pattern):
            
            if j in dect3.keys() and dect3[j] !=i:
                return False
            dect3[j]=i
            print(dect3.values())
        return value1==value2

        


        

       
        


