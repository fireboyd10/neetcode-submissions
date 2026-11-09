class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        result = 0
        for num in mySet:
            count = 1
            if num - 1 not in mySet:
                while num + 1 in mySet:
                    count+=1
                    num += 1
            result = max(result, count)
        return result