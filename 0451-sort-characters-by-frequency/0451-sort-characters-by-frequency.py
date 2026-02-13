from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)

        # sort characters based on frequency (descending)
        chars = sorted(counter.keys(), key=lambda c: counter[c], reverse=True)

        result = ""
        for ch in chars:
            result += ch * counter[ch]

        return result


        
        