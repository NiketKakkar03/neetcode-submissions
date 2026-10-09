class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     for j in range(len(numbers)):
        #         if i != j:
        #             if numbers[i] + numbers[j] == target:
        #                 return [i+1, j+1]

        # hm = defaultdict(int)
        # for i in range(len(numbers)):
        #     tmp = target - numbers[i]
        #     if hm[tmp]:
        #         return [hm[tmp], i+1]
        #     hm[numbers[i]] = i+1
        # return []

        l, r = 0, len(numbers)-1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l + 1, r + 1]
            elif sum > target:
                r -= 1
            else: l += 1

