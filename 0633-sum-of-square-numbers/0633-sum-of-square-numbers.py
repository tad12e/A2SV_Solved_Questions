class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        if c==1 or c==2 or c==0: return True

       


        for i in range((c//2)):
            if c-(i**2) <0:
                break
            
            num=(c-(i**2))**0.5
        
            if int(num)**2==(c-(i**2)):
                return True
        return False
        