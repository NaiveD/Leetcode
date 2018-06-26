# 暴力法
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            # 把 target == nums[i] + nums[j] 放在这一层循环比较快
            a = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == a: # 如果是 if target == nums[i] + nums[j] 会超时
                    return [i, j]