class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        output=0

        sor=sorted(nums)
        lon=0

        for i in range(len(sor)-1):
            
            
            if sor[i]+1==sor[i+1]:
                lon=lon+1
                print(lon)
                output=max(output, lon)
            elif sor[i]==sor[i+1]:
                pass
           
            else:
                lon=0
        return output+1


