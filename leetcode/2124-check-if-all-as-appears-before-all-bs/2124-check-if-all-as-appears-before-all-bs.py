class Solution:
    def checkString(self, s: str) -> bool:
        b=False

        for i in s:

            if b==False and i=="b":
                b=True 
            elif b==True and i=="a":
                return False
        return True
