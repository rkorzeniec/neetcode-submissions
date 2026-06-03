class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        shortest = min(strs)

        for i in range(len(shortest)):
            for j in range(len(strs)):
                if strs[j][i] != shortest[i]:
                    return result
            result += shortest[i]

        return result