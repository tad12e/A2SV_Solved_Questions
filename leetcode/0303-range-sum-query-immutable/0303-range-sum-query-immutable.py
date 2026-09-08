class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums

        

    def sumRange(self, left: int, right: int) -> int:
        sume=0

        for i in range(left, right+1):
            sume+=self.nums[i]
        return sume
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)