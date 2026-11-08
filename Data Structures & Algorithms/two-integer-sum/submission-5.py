class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i, num in enumerate(nums):
            dif = target - num
            if dif in a and a[dif] != i:
                if a[dif] < i:
                    return [a[dif], i]
                else: return [i, a[dif]]
            a[num] = i