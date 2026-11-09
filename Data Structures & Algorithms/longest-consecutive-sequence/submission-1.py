class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet  = set(nums)
        result = 0
        for n in nums:
            count = 1
            m = n 
            if n-1 not in mySet:
                while m + 1 in mySet:
                    m += 1
                    count += 1  
            result = max(result, count)
        return result