from collections import Counter
import math
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        l1=len(nums)
        dect=Counter(nums)
        h=dect.most_common(1)[0][0]
        d=dect.most_common(1)[0][1]
        #print(h, d)
        print(3/2)
        H=0


        for i in range(l1):
            #left = nums[0:i+1]
           # right = nums[i+1:l1]
            if nums[i]==h:
                H+=1
               
            
            if H>(i+1)//2 and (d-H)>(l1-i-1)//2:
                return i
        return -1
            
        