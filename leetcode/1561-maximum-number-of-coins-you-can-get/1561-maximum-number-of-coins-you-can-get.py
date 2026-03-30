class Solution:
    def maxCoins(self, piles: List[int]) -> int:


        piles.sort()


        ans=0
        cntrl=len(piles)-2
        another=0

        while cntrl >0 and another < len(piles) //3 :
            print(piles[cntrl])
            ans+=piles[cntrl]
            another+=1

            cntrl-=2
      
        return ans