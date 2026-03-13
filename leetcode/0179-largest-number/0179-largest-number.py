class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert integers to strings
        store = [str(num) for num in nums]
        
        # Custom sort with comparator
        # Sort in descending order based on concatenation
        from functools import cmp_to_key
        store.sort(key=cmp_to_key(lambda a, b: -1 if a+b > b+a else 1))
        
        # 🔹 handle all zeros case
        if store[0] == "0":
            return "0"
        
        # Concatenate all strings
        ans = "".join(store)
        
        return ans