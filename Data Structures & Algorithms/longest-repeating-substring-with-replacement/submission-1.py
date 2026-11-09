class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        d = {}
        left = 0
        for right in range(len(s)):
            d[s[right]] = 1 + d.get(s[right], 0)
            if (right-left+1) - max(d.values()) > k:
                d[s[left]] -= 1
                left+=1
            result = max(result, right - left + 1)
    
        return result