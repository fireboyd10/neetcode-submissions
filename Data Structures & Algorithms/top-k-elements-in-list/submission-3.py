class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        result = []
        for n in nums:
            if n not in counts:
                counts[n] = 1
            else: counts[n]+=1

        stack = []
        for n in counts:
            stack.append([counts[n], n])

        stack.sort()
        while k>0:
            pair = stack.pop()
            result.append(pair[1])
            k-=1
        return result