class Solution(object):
    def isPalindrome(self, s):
        cleaned_s = ''.join(ch.lower() for ch in s if ch.isalnum())
        if cleaned_s == cleaned_s[::-1]:
            return True
        return False

s = input().strip()[1:-1]   

sol = Solution()
print(sol.isPalindrome(s))
