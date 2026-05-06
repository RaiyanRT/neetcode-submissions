class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # pop all integers from the list if an operand happends then do the calc

        answer = []

        for char in tokens:
            if char == "+":
                answer.append(answer.pop() + answer.pop())
            elif char == "-":
                new = answer.pop()
                original = answer.pop()
                answer.append(original - new)
            elif char == "*":
                answer.append(answer.pop() * answer.pop())
            elif char == "/":
                new = answer.pop()
                original = answer.pop()
                answer.append(int(original/new))
            else:
                answer.append(int(char))

        return answer[0]