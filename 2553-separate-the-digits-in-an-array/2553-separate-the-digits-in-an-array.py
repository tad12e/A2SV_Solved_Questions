class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        st=""

        for i in nums:
            st=st+str(i)
        for i in st:
            res.append(int(i))
        return res
            
            

        