'''
Given a string s containing just the characters '(', ')', '{', '}', '[', and ']', determine if the input string is valid.

A string is considered valid if:

Open brackets are closed by the same type of brackets.

Open brackets are closed in the correct order.

Each closing bracket has a matching corresponding opening bracket.
'''

mapping = {')': '(', '}': '{', ']': '['}

def is_valid(chars: list[chr]) -> bool:
    opening_char = mapping.values()
    closing_char = mapping.keys()
    stack = []
    for index_of_char, char in enumerate(chars):
        if char in opening_char:
            stack.append(char)
        elif char in closing_char:
            if len(stack) != 0 and stack[-1] == mapping[char]:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    return False
