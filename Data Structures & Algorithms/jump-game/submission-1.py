class Solution:
    def canJump(self, nums: List[int]) -> bool:
        steps = nums[0]

        for i in range(1, len(nums)):
            if steps == 0:
                return False
            steps -= 1

            if nums[i] > steps:
                steps = nums[i] 

        return True