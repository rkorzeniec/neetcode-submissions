class Solution:
    DELIMITER = "#"

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            result += f"{len(word)}{self.DELIMITER}{word}"

        return result

    def decode(self, s: str) -> List[str]:
        result: list[str] = []

        i = 0
        while i < len(s):
            word_len = ""
            while s[i] != self.DELIMITER:
                word_len += s[i]
                i += 1

            i += 1 # skip delimeter

            word = s[i:i+int(word_len)]
            i += int(word_len)
            result.append(word)

        return result
