class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ""
        if len(t) > len(s):
            return result

        need_chars = {}
        for char in t:
            need_chars[char] = need_chars.get(char, 0) + 1

        need_len = len(need_chars)
        matches = 0
        result_len = len(s) + 1

        l = 0
        window_chars = {}
        for r in range(len(s)):
            char = s[r]
            window_chars[char] = window_chars.get(char, 0) + 1

            if char in need_chars and window_chars[char] == need_chars[char]:
                matches += 1
            
            while matches == need_len:
                if (r - l + 1) < result_len:
                    result_len = r - l + 1
                    result = s[l:r+1]
                    
                char = s[l]
                window_chars[char] -= 1

                if char in need_chars and window_chars[char] < need_chars[char]:
                    matches -= 1

                l += 1

        return result