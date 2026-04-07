from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        res = [-1] * len(nums2)   

     
        for i in range(len(nums2)):

            while stack and nums2[i] > nums2[stack[-1]]:
                res[stack[-1]] = nums2[i]
                stack.pop()

            stack.append(i)

        
        next_map = {}

        for i in range(len(nums2)):
            next_map[nums2[i]] = res[i]
        ans = []

        for num in nums1:
            ans.append(next_map[num])

        return ans
        



        