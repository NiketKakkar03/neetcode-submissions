class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        A = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in A:
                return [A[diff], i]
            A[num] = i
        
        