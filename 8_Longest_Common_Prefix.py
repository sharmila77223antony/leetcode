class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        prefix = []
        
        for ch in zip(*strs):
            if len(set(ch)) == 1:
                prefix.append(ch[0])
            else:
                break
                
        return ''.join(prefix)


strs = input()
strs = strs.strip()[1:-1].replace('"', '').split(',')

sol = Solution()
print(sol.longestCommonPrefix(strs))
