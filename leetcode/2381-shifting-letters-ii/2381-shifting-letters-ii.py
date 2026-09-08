class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        # Size n + 1 prevents IndexError when updating end + 1
        diff = [0] * (n + 1)

        # 1. Populate difference array
        for start, end, direction in shifts:
            val = 1 if direction == 1 else -1
            diff[start] += val
            diff[end + 1] -= val

        # 2. Compute prefix sum to get total shifts per index
        current_shift = 0
        result = []
        for i in range(n):
            current_shift += diff[i]
            
            # 3. Calculate 0-25 alphabet index and apply shift with modulo
            original_idx = ord(s[i]) - ord('a')
            new_idx = (original_idx + current_shift) % 26
            
            # 4. Convert back to character
            result.append(chr(ord('a') + new_idx))

        return "".join(result)