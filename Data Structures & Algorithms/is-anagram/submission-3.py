class Solution:
    def _build_cache(self, s: str) -> dict[str]:
        cache = {}

        for char in s:
            if char in cache:
                cache[char] += 1
            else:
                cache[char] = 1
        
        return cache

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        cache_s = self._build_cache(s)
        cache_t = self._build_cache(t)
        
        for char in cache_s.keys():
            if char not in cache_t:
                return False

            if cache_s[char] != cache_t[char]:
                return False

        return True

        