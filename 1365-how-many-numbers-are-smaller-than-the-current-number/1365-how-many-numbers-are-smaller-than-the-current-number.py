class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
     
        freq = [0] * 101
        for num in nums:
            freq[num] += 1
      
        prefix = [0] * 101
        for i in range(1, 101):
            prefix[i] = prefix[i-1] + freq[i-1]
        
    
        return [prefix[num] for num in nums]




        