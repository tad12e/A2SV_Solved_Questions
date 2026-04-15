class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        left, right=0,0

        arr=[]

        while left <len(nums1) and right <len(nums2):
            if nums1[left]<nums2[right]:
                arr.append(nums1[left])
                left+=1
            else:
                arr.append(nums2[right])
                right+=1

        arr.extend(nums1[left:])
        arr.extend(nums2[right:])
        if len(arr)%2==0:
            indx1=len(arr)//2
            indx2=indx1-1
            elm1=arr[indx1]
            elm2=arr[indx2]
            median= (elm1+elm2)/2
            return median
        else:
            indx=len(arr)//2
            return arr[indx]