class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        #create hashmaps
        prevMap = {}

        #checking for sums that would equal to target
        for i, n in enumerate(nums):
            pair = target - n

            if pair in prevMap:
                return [prevMap[pair], i]
            prevMap[n] = i
        
        return

obj = Solution()

nums = [2,11,15,7]
target = 9

print(obj.twoSum(nums, target))