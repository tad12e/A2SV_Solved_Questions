class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        # prefix differences
        diff_map = {(0, 0): -1}  # (diff_ab, diff_ac) -> first index
        count_a = count_b = count_c = 0
        max_len = 0

        for i, ch in enumerate(s):
            if ch == 'a':
                count_a += 1
            elif ch == 'b':
                count_b += 1
            else:
                count_c += 1

            diff_ab = count_a - count_b
            diff_ac = count_a - count_c

            if (diff_ab, diff_ac) in diff_map:
                max_len = max(max_len, i - diff_map[(diff_ab, diff_ac)])
            else:
                diff_map[(diff_ab, diff_ac)] = i

        return max_len
