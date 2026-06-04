class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"}": "{", "]": "[", ")": "("}
        open_brackets = set(["{", "(", "["])
        stack = []

        for char in s:
            if char in open_brackets:
                stack.append(char)
            elif not stack:
                return False
            elif brackets[char] != stack.pop():
                return False
        
        return len(stack) == 0