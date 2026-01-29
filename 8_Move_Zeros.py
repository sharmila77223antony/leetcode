class Solution(object):
    def moveZeroes(self, nums):
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)


nums = eval(input())

Solution().moveZeroes(nums)

print(nums)
