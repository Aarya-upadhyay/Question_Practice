class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        """a=-1
        b=1
        for i in range(n+1):
            c=a+b
            a=b
            b=c
        return c
        """
        return self.fib(n-1)+self.fib(n-2)
