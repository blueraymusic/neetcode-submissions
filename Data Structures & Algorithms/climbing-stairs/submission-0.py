class Solution:
    def climbStairs(self, n: int) -> int:
        def fib(n:int) -> int:
            s1,s2 = 1,1 
            for _ in range(n):
                temp = s2
                s2 = s1 + s2 
                s1 = temp
            
            return s1
        return fib(n)
        