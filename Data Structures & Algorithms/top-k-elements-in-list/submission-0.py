class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts: dict[int:int] = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            buckets[freq].append(num)

        result = []
        for freq in range(len(buckets)-1, 0, -1):
            for num in buckets[freq]:
                result.append(num)

                if len(result) == k:
                    return result


