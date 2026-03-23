class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = []
        for k in range(n, 0, -1):
            i = arr.index(k)

            if i == k - 1:
                continue

            if i != 0:
                arr[:i+1] = arr[:i+1][::-1]
                res.append(i+1)

            arr[:k] = arr[:k][::-1]
            res.append(k)
        return res