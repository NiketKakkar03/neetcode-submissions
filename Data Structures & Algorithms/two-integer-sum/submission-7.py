class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            if (target-nums[i] in nums[i+1:len(nums)]):
                return [i, nums[i+1:len(nums)].index(target-nums[i]) + i + 1]
        