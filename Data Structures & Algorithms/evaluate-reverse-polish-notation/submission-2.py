class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator_keys = set(["+", "-", "*", "/"])
        operators = {
            "+": lambda a, b: int(a) + int(b),
            "-": lambda a, b: int(a) - int(b),
            "*": lambda a, b: int(a) * int(b),
            "/": lambda a, b: int(int(a) / int(b))
        }

        for t in tokens:
            if t in operator_keys:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(str(operators[t](op1, op2)))
            else:
                stack.append(t)

        return int(stack[-1])