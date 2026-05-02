"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        ans=0
        visited=set()


        def dfs(id, importance, subordinate):
            nonlocal ans
            ans+=importance
            visited.add(id)
            if not subordinate:
                return
            

            for i in subordinate:
                for j in employees:
                    id2, importance, subordinate=j.id, j.importance, j.subordinates
                    if id2==i and id2 not in visited:
                        dfs(i,importance, subordinate)

            #return ans
        for i in employees:
            id1, importance, subordinate=i.id, i.importance, i.subordinates
            if id1==id:
                dfs(id1, importance, subordinate)
        return ans

        



            
            
            

            
        