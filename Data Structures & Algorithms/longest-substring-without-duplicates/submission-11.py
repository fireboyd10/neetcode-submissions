class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        d = set()
        result = 0
        for right in range(len(s)):
            while s[right] in d:
                d.remove(s[left])
                left+=1
            d.add(s[right])
            result = max(result, right - left + 1)
        return result