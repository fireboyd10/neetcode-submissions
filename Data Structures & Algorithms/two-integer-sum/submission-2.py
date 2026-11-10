class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i in range(len(nums)):
            a[nums[i]] = i
            dif = target - nums[i]
            if dif in a and a[dif] != i:
                if a[dif] < i:
                    return [a[dif], i]
                else: return [i, a[dif]]
        return