class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res=[0]*len(s)

        for i, j in zip(s, indices):
            res[j]=i
        
        return "".join(res)

        