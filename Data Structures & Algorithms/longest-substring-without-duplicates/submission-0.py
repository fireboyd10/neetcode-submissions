class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0 
        left = 0
        count = 0
        d = {}
        d[s[left]] = 1
        for right in range(1, len(s)):
            if s[right] in d:
                count = 0
                left = right
                d = {}
            d[s[right]] = 1
            count+=1
            if max < count: 
                max = count
        return max