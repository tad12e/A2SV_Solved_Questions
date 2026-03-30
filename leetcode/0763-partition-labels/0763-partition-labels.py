from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        freq=Counter(s)


        res=[]
       
        curr=""

        count=0
        st=0

        

        for i in range(len(s)):
            if s[i] not in curr:
                st+=1
            

            curr+=s[i]
            freq[s[i]]-=1
            if freq[s[i]]==0:
                count+=1
        

            if count==st:
                res.append(len(curr))
                curr=""
        return res



        