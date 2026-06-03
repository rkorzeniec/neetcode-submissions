# Brute force aproach
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        i = 0
        chars = set()
        max_chars = 0

        while i < len(s):
            j = i
            while j < len(s):
                if s[j] in chars:
                    break

                chars.add(s[j])
                j += 1

            max_chars = max(len(chars), max_chars)
            chars = set()
            i += 1

        return max_chars
