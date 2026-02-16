from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #n=len(strs)

        
        #res=[]
        list1=strs
        dect=defaultdict(list)
        for i in range(len(list1)):
            #detc[i]+=1
            dect["".join(sorted(strs[i]))].append(strs[i])
        print(dect)

        res=[value for value in dect.values()]
        return res
            
            

                

        