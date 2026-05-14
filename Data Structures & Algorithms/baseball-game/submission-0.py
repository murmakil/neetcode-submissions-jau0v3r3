class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for item in operations:
            if item == "+":
                stack.append(sum(stack[-2:]))
            elif item == "C":
                stack.pop()
            elif item == "D":
                stack.append(2 * stack[-1])
            else:
                stack.append(int(item))
        return sum(stack)