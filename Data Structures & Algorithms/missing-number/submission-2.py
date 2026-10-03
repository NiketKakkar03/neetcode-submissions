class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums.sort()

        # for i in range(len(nums)):
        #     if i != nums[i]:
        #         return i
        # return len(nums)
        
        return sum(range(len(nums)+1)) - sum(nums)
            

        