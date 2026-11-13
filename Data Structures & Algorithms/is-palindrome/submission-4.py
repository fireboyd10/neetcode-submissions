class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=[]
        for c in s:
            if c.isalnum():
                n.append(c.lower())
        new = n[::-1]

        return new == n