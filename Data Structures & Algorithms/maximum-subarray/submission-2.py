class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        Sum = nums[0]
        curr = 0
        i = 0
        while i < len(nums):
            curr += nums[i]
            Sum = max(Sum, curr)

            if curr < 0: curr = 0

            i+=1
            

        return Sum 