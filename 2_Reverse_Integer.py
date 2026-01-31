class Solution(object):
    def reverse(self, x):
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x != 0:
            n = x % 10
            res = (res * 10) + n
            x = x // 10
            
        res *= sign
        
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res

x = int(input())

sol = Solution()
print(sol.reverse(x))
