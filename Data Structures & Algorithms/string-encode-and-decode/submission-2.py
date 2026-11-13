class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + '#' + word
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded=[]
        c = 0
        while c < len(s):
            j = c
            while s[j] != '#':
                j+=1
            length = int(s[c:j])
            word = s[j+1: j+1+length]
            decoded.append(word)
            c = j + 1 + length
        return decoded
