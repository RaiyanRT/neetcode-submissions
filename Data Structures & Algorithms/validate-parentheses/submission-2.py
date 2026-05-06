class Solution:
    def isValid(self, s: str) -> bool:
        # Pop out the back elements and see if they make a string that is the same as the first elements 
        # char_list = []
        # stack = []
        # mid_point = len(s) // 2

        # for char in s:
        #     char_list.append(char)

        # while mid_point != 0:
        #     stack.append(char_list.pop())
        #     mid_point -= 1

        # for index in range(len(stack)):
        #     if stack[index] == ']':
        #         stack[index] = '['
        #     if stack[index] == '}':
        #         stack[index] = '{'
        #     if stack[index] == '(':
        #         stack[index] = ')'
        # []{}()
        # if char_list == stack:
        #     return True

        # return False

        stack = []

        brackets = {')': '(', '}' : '{', ']':'['}

        for char in s:
            if char in brackets: #Keys or closed brackets
                if len(stack) == 0:
                    return False
                right_value = stack.pop()
                if right_value != brackets[char]:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0 







