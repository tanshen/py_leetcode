class Solution:

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        if len(nums) < 3:
            return ret
        else:
            nums.sort()
            i = 0
            while i < len(nums)-2:
                k = len(nums) - 1
                j = i+1
                while j < k:
                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] == 0:
                        ret.append((nums[i], nums[j], nums[k]))
                        j += 1
                        k -= 1
                        while j < k and nums[k+1] == nums[k]:
                            k -= 1
                        while j < k and nums[j-1] == nums[j]:
                            j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                i += 1
                while i < len(nums) - 2 and nums[i] == nums[i-1]:
                    i += 1
        return list(set(tuple(ret)))


nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
s = Solution()
print(s.threeSum(nums))


