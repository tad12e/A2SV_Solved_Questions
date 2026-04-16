class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)


        def helper(capacity):

            hour_needed=0
           


            for pile in piles:
                hour_needed+=(ceil(pile/capacity))


                
            
            return hour_needed<=h

        while left<right:

            mid=(left+right)//2

            if helper(mid):
                right=mid

            else:
                left=mid+1


        return left
        