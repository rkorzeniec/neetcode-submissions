class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}
        result = 0

        l = 0
        max_f = 0
        for r in range(len(s)):
            chars[s[r]] = chars.get(s[r], 0) + 1
            max_f = max(max_f, chars[s[r]])

            while (r - l + 1) - max_f > k:
                chars[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)

        return result