# 哈希表
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # make a dictionary
        d = {}

        # a cycle from nums[0] to nums[len(nums)]
        for i in range(len(nums)):
        	# first, {nums[i]: i}
        	d[nums[i]] = i

        	if (target - nums[i] in d) and ((target - nums[i]) != nums[i]):
        		result = [d[target-nums[i]], d[nums[i]]]
        		return result
        	if target - nums[i] == nums[i]:
        		result = [i, nums.index(nums[i], i+1)]
        		return result

nums1 = [3, 3]
target1 = 6
out = Solution().twoSum(nums1, target1)
print(out)

# result: [0, 4]