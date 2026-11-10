class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            d[num]=i
            dif = target - num
            if dif in d and dif!=num:
                return [d[dif], d[num]]
            
                
        