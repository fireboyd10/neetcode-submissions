class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        left = 0
        count = 0
        d = {}

        for right in range(len(s)):
            if s[right] in d and d[s[right]] >= left:
                left = d[s[right]] + 1

            d[s[right]] = right
            count = right - left + 1

            if max < count:
                max = count

        return max