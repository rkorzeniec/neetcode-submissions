class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = [0] * 26
        max_chars = 0
        max_f = 0 # max frequency

        l = 0 # left pointer
        r = 0 # right pointer
        while r < len(s):
            idx = ord(s[r]) - ord("A")
            chars[idx] += 1
            max_f = max(max_f, chars[idx])

            window_len = r - l + 1
            replacements = window_len - max_f

            if replacements <= k:
                max_chars = max(max_chars, window_len)
            else:
                chars[ord(s[l]) - ord("A")] -= 1
                l += 1
                
            r += 1
        return max_chars