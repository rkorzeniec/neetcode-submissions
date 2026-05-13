class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = defaultdict(list)

        for word in strs:
            counts = [0] * 26

            for char in word:
                index = ord(char) - ord("a")
                counts[index] += 1

            cache[tuple(counts)].append(word)
            
        return list(cache.values())