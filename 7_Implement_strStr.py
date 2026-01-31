class Solution(object):
    def strStr(self, haystack, needle):
        index = haystack.find(needle)
        if index != -1:
            return index
        else:
            return -1


haystack = input().strip()[1:-1]  
needle = input().strip()[1:-1]    

sol = Solution()
print(sol.strStr(haystack, needle))
