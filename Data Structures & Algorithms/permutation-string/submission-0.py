class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_chars = [0]*26
        for s in s1:
            idx = ord(s)-ord("a")
            s1_chars[idx] += 1

        l = 0
        r = len(s1) - 1
        while r < len(s2):
            s2_chars = [0]*26
            for s in s2[l:r+1]:
                idx = ord(s)-ord("a")
                s2_chars[idx] += 1

            if s1_chars == s2_chars:
                return True

            l += 1
            r += 1

        return False