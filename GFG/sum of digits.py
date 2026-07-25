class Solution:
    def sumOfDigits(self, n):
        # code here
        if n==0:
            return 0
        d=n%10
        return (d+self.sumOfDigits(n//10))
