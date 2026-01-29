class Solution(object):
    def rotate(self, nums, k):
        if not nums:
            return

        n = len(nums)
        k %= n

        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])


nums = eval(input())
k = int(input())

Solution().rotate(nums, k)

print(nums)
