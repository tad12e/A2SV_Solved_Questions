class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)

        

        def helper(capacity):
            day_needed=1
            wight=0


            for weight in weights:
                wight+=weight


                if wight>capacity:
                    wight=weight
                    day_needed+=1

            return day_needed<=days

        ans=-1

        while left<right:


            mid=(left+right)//2


            if helper(mid):
                right=mid
                ans=mid
            else:
                left=mid+1
        return left

        