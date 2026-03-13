class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        dect={}
        f=len(nums2)


        for i in range(len(nums2)):
            if nums2[i] in nums1:

                dect[nums2[i]]=i
               
        for i in nums1:
            if dect[i]+1<f:
                
                for k in nums2[dect[i]+1:]:
                    if k>i:
                        ans.append(k)
                        break
                
                else:
                    ans.append(-1)
            else:
                ans.append(-1)
        print(dect)
       

        return ans
            