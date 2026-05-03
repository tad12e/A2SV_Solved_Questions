class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):return False

        new=s+s
        if goal in new:
            return True
        return False       

    
        