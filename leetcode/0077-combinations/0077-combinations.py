class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def comp(path, i):
            if len(path) == k:
                ans.append(path.copy())  # also safer
                return

            for j in range(i, n + 1):
                path.append(j)
                comp(path, j + 1)
                path.pop()

        comp([], 1)
        return ans
        