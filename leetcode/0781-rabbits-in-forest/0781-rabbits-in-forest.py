from collections import Counter

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq=Counter(answers)

        total=0

        pure=set(answers)


        for rabbit in pure:

            if rabbit==0:
                total+=freq[rabbit]
            elif freq[rabbit]<=rabbit+1:
                total+=freq[rabbit]+(rabbit+1-freq[rabbit])
            else:
            
                diff=freq[rabbit]
                while diff>=rabbit+1:
                    total+=rabbit+1
                    diff-=rabbit+1
                if diff>0:
                    total+=diff+(rabbit+1-diff)
                
                    
            

        return total



        