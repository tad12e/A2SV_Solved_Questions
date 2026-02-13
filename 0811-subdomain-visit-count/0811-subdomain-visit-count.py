#import collections
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dect=defaultdict(int)
        


        for i in cpdomains:
            #number=0
            s=[]
            #indx=j

            for j in range(len(i)):
                if i[j]==" ":
                    global number
                    number=int(i[:j])
                    dect[(i[j+1:])]+=number
                    print(number)
                   #indx=j
                elif i[j]==".":
                    dect[i[j+1:]]+=number
        res=[f"{value} {key}" for key, value in dect.items()]
        return res



     







  





        