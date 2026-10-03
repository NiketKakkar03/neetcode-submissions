class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # result = []

        # for i in range(n):
        #     product = 1
        #     for j in range(n):
        #         if nums[i] != nums[j]:
        #             product *= nums[j]
        #     result.append(product)
        # return result
        n = len(nums)
        result = [1] * n

        pre = post = 1
        for i in range(n):
            result[i] = pre
            pre *= nums[i]
        
        for j in range(n-1, -1, -1):
            result[j] *= post
            post *= nums[j]
        return result
        



             