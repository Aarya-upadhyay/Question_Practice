class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        # 1. skip spaces
        while i < n and s[i] == " ":
            i += 1

        # 2. sign
        sign = 1
        if i < n and (s[i] == "+" or s[i] == "-"):
            if s[i] == "-":
                sign = -1
            i += 1

        # 3. digits
        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            num = num * 10 + digit
            i += 1

        num *= sign

        # 4. clamp to 32-bit range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num
class Solution:
    def myAtoi(self, s: str) -> int:
        # 1. Ignore leading whitespace
        s = s.lstrip()
        if not s:
            return 0
        
        # 2. Determine signedness
        sign = 1
        index = 0
        if s[0] == '-':
            sign = -1
            index = 1
        elif s[0] == '+':
            index = 1
            
        # 3. Conversion
        res = 0
        while index < len(s) and s[index].isdigit():
            # Convert char to int and add to result
            res = res * 10 + int(s[index])
            index += 1
            
        # Apply the sign
        res *= sign
        
        # 4. Rounding (32-bit signed integer range)
        # INT_MIN = -2^31, INT_MAX = 2^31 - 1
        INT_MIN, INT_MAX = -2147483648, 2147483647
        
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
            
        return res
