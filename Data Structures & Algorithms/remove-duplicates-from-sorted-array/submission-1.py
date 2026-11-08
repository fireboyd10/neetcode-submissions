class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new = sorted(set(nums))
        k = 0
        for i, n in enumerate(new):
            nums[i] = n
            k += 1
        return k