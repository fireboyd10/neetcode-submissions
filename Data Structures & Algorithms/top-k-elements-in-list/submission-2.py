class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1

        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])

        for n in counts:
            frequency = counts[n]
            buckets[frequency].append(n)

        result = []

        for i in range(len(nums), 0, -1):
            for n in buckets[i]:
                result.append(n)

                if len(result) == k:
                    return result