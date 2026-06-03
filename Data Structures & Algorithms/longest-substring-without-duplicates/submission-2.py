# Sliding window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        chars = set()
        max_chars = 0

        while r < len(s):
            if s[r] not in chars:
                chars.add(s[r])
                r += 1
                max_chars = max(r - l, max_chars)
            else:
                chars.remove(s[l])
                l += 1

        return max_chars