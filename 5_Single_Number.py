class Solution(object):
    def singleNumber(self, nums):
        res = set()
        for i in nums:
            if i in res:
                res.remove(i)
            else:
                res.add(i)
        return res.pop()


nums = eval(input())

result = Solution().singleNumber(nums)

print(result)
