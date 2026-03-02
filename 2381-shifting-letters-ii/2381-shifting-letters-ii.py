class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        diff = [0] * (len(s) + 1)
        for shift in shifts:
            l, r, d = shift
            if d == 1:
                diff[l] += 1
                diff[r + 1] -= 1
            else:
                diff[l] -= 1
                diff[r + 1] += 1
            
        current = 0
        shifted = []

        for i, char in enumerate(s):
            current += diff[i]
            val = ord(char) - ord("a")
            new_val = (current + val) % 26
            shifted.append(chr(new_val + ord("a")))
        
        return "".join(shifted)