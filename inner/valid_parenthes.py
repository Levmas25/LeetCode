# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
def valid_parenthes(s: str) -> bool:
    stack = list()

    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]' and len(stack) == 0:
                return False
        elif char == ')' and stack[-1] != '(':
            return False
        elif char == '}' and stack[-1] != '{':
            return False
        elif char == ']' and stack[-1] != '[':
            return False
        else:
            stack.pop(-1)

    return len(stack) == 0

print(valid_parenthes('(())'))
print(valid_parenthes('(()'))
print(valid_parenthes('([))'))
print(valid_parenthes('(({[]}))'))
        