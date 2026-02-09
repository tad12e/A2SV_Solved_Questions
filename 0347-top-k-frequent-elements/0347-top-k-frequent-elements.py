from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]

        numsd=Counter(nums)

        mo=numsd.most_common(k)
        #print(mo)
        return [key for key, j in mo]

        

        

        
        