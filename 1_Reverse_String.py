class Solution(object):
    def reverseString(self, s):
        first = 0
        last = len(s) - 1
        
        while first < last:
            s[first], s[last] = s[last], s[first]
            first += 1
            last -= 1


s = input().strip()[1:-1].replace('"', '').split(',')

sol = Solution()
sol.reverseString(s)
print(s)
