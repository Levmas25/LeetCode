'''Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

1. Whitespace: Ignore any leading whitespace (" ").
2. Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
3. Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. 
If no digits were read, then the result is 0.
4. Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. 
Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.'''

def myAtoi(s: str) -> int:
    '''Robit no govnocod👎👎👎'''
    res = 0
    sign = 1

    i = 0 
    while i != len(s):

        if i != len(s) - 1 and s[i] in '+-' and not s[i + 1].isdigit():
            break 
        
        if i > 0 and not s[i].isdigit() and s[i - 1].isdigit():
            break

        if s[i] == ' ' or (s[i] == '0' and res == 0):
            i += 1
            continue

        if (s[i] == '-' and i > 0 and s[i - 1] == ' ') or (s[i] == '-' and i == 0):
            sign = -1
            i += 1
            continue

        if (s[i] == '+' and i > 0 and s[i - 1] == ' ') or (s[i] == '+' and i == 0):
            sign = 1
            i += 1
            continue

        if not s[i].isdigit():
            return sign * res 
        
        res = (res * 10) + int(s[i])
        i += 1

    if res > 2 ** 31 - 1 and sign == 1:
        return 2 ** 31 - 1

    if res > 2 ** 31 and sign == -1:
        return -2 ** 31 
        
    return sign * res


print('\n')
print(myAtoi('42'))
print(myAtoi(' -042'))
print(myAtoi('1337c0d3'))
print(myAtoi('0-1'))
print(myAtoi('words and 987'))


def solution(s: str) -> int:
    '''Robit i ne govnocod👍👍👍💪💪💪💪🍺🍺🍺🍺'''
    s = s.strip()
    if not s:
        return 0
    i = 0
    sign = 1
    result = 0
    if s[i] == '-' or s[i] == '+':
        sign = -1 if s[i] == '-' else 1
        i += 1
    while i < len(s) and s[i].isdigit():
        digit = int(s[i])
        if result > (2**31 - 1 - digit) // 10:
            return 2**31 - 1 if sign == 1 else -2**31
        result = result * 10 + digit
        i += 1
    return sign * result

            