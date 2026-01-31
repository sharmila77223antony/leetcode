class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        freq = {}
        
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
            
        for ch in t:
            if ch not in freq or freq[ch] == 0:
                return False
            freq[ch] -= 1
            
        return True


s = input().strip()[1:-1]  
t = input().strip()[1:-1]   

sol = Solution()
print(sol.isAnagram(s, t))
