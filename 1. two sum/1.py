import json

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
            if target - nums[i] == nums[i] and (nums.count(nums[i]) == 2):
                result = [i, nums.index(nums[i], i+1)]
                return result

def stringToIntegerList(input):
    return json.loads(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);
            line = next(lines)
            target = int(line);
            
            ret = Solution().twoSum(nums, target)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()