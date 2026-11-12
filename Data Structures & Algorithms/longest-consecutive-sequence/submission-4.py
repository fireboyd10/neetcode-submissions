class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        total = 0

        for n in nums:
            m = n
            count = 1
            if m-1 not in mySet:            
                while m + 1 in mySet:
                    m += 1
                    count+=1
            total = max(count, total)
        return total