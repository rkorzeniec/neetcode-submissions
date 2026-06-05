class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: list[tuple[int, int]] = [(temperatures[0], 0)]
        result = [0] * len(temperatures)

        i = 1
        while len(stack) != 0:
            if len(temperatures) - 1 < i:
                return result

            while len(stack) != 0 and temperatures[i] > stack[-1][0]:
                _, idx = stack.pop()
                result[idx] = i - idx

            stack.append((temperatures[i], i))
            i += 1

        return result