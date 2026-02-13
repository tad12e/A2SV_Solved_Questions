from collections import Counter

class Solution:
    def findCommonResponse(self, responses):
        freq = Counter()

        # count per person
        for person in responses:
            freq.update(set(person))

        # find best answer
        best_word = ""
        best_count = 0

        for word, count in freq.items():
            if count > best_count or (count == best_count and word < best_word):
                best_word = word
                best_count = count

        return best_word
