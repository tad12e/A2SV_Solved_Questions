class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res=[]
        
        dect={}



        for i in range(len(list1)):
            if list1[i] in list2:
                dect[list1[i]]= i+list2.index(list1[i])
        idx=min(dect.values())
        for key, value in dect.items():
            if value==idx:
                res.append(key)
        return res  

        