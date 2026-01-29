class Solution(object):
    def containsDuplicate(self, nums):
        res = set()
        for i in range(len(nums)):
            if nums[i] in res:
                return True
            res.add(nums[i])
        return False


nums = eval(input())

result = Solution().containsDuplicate(nums)

print(result)
