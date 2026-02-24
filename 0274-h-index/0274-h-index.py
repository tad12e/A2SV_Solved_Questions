
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if [0]*len(citations)==citations:
            return 0
           


        citations.sort()
        i=0
        print(citations)

        while i<len(citations):
            if citations[i]>=len(citations)-i:
                return len(citations)-i
            i+=1
           
        