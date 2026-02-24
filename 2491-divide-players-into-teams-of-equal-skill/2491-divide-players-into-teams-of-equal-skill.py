class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        skill.sort()

        j=len(skill)-1
        res=[]

        r=skill[0]+skill[-1]
        ans=0

        for i in range(len(skill)):
            if skill[i]+skill[j] != r:
                return -1
            else:
                res.append((skill[i], skill[j]))
            j-=1
        print(res)
        for k, l in res:
            ans+=(k*l)
        return ans//2
        
        



        