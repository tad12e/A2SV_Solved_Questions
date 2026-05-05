from collections import deque
class Solution:
    def findOrder(self, numCourses: int, pre: List[List[int]]) -> List[int]:
        


        graph=defaultdict(list)
        indgree=[0]*numCourses

        for  u, v in pre:
            graph[v].append(u)

        for u,v in pre:
            indgree[u]+=1
        qeue=deque(i for i in range(len(indgree)) if indgree[i]==0)
        order=[]


        while qeue:
            curr=qeue.popleft()
            order.append(curr)

            for i in graph[curr]:
                indgree[i]-=1
                if indgree[i]==0:
                    qeue.append(i)
        
        return order if len(order) == numCourses else []



        

        

        



        