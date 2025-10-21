from functools import cache # python 3.9+

class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n in [1, 2]:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)