class Solution:
    def isPalindrome(self, s):

        if len(s) <= 1:
            return True

        if s[0] != s[-1]:
            return False

        return self.isPalindrome(s[1:-1])
      
