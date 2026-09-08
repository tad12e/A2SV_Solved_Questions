class Solution:
    def countCommas(self, n: int) -> int:

        length=len(str(n))

        if n<1000:
            return 0

        return n-1000+1


        



        