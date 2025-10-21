class Solution:
    def climbStairs(self, n: int) -> int:
        # Create a cache to store results
        cache = {}
        return self.climb_helper(n, cache)

    def climb_helper(self, n: int, cache: dict) -> int:
        # If we've solved this before, return the stored result
        if n in cache:
            return cache[n]
        
        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
        # Note: A base case for n=0 returning 1 is also common
        # if you adjust the logic, but your way works.

        # Compute, store in cache, and then return
        result = self.climb_helper(n - 1, cache) + self.climb_helper(n - 2, cache)
        cache[n] = result
        return result