class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"}": "{", "]": "[", ")": "("}
        open_brackets = set(["{", "(", "["])
        stack = []

        for char in s:
            if char in open_brackets:
                stack.append(char)
            else:
                if not stack:
                    return False
                stack_char = stack.pop()
                if brackets[char] != stack_char:
                    return False
        
        return len(stack) == 0