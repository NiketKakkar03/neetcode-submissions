class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums):
            second = target - n
            if second in hashmap:
                return [hashmap[second], i]
            hashmap[n] = i
        