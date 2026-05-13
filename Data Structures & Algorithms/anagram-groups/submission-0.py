class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache: dict[tuple[int]:list[str]] = {}

        for word in strs:
            counts = [0 for _ in range(26)]

            for char in word:
                index = ord(char) - 97
                counts[index] += 1

            counts_tuple = tuple(counts)
            if counts_tuple in cache:
                cache[counts_tuple].append(word)
            else:
                cache[counts_tuple] = [word]
            
        return list(cache.values())