class Solution:
    def isPalindrome(self, s: str) -> bool:
        original = ""
        for char in s:
            if 'A' <= char <= 'z' or '0' <= char <= '9':
                original+=char.lower()
        reversed = original[::-1]
        if original == reversed:
            return True
        else: 
            return False