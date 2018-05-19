class Solution:

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ret = nums[0] + nums[1] + nums[-1]
        value = abs(nums[0] + nums[1] + nums[-1] - target)
        i = 0

        while i < len(nums)-2:
            k = len(nums)-1
            j = i+1
            while j < k:
                if abs(nums[i] + nums[j] + nums[k] - target) < value:
                    ret = nums[i] + nums[j] + nums[k]
                    value = abs(nums[i] + nums[j] + nums[k] - target)

                if nums[i] + nums[j] + nums[k] - target > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] - target < 0:
                    j += 1
                else:
                    # value = 0
                    return nums[i] + nums[j] + nums[k]

            i += 1
            while i < len(nums)-2 and nums[i] == nums[i-1]:
                i += 1
        return ret

s = Solution()
nums = [-1, 2, 1, -4]
target = 1
print(s.threeSumClosest(nums, target))
