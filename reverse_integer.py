def reverseInteger(x: int) -> int:
    from math import log10, ceil
    if x == 0: return 0
    sign = 1 if x >= 0 else -1
    x *= sign
    new = 0
    i = ceil(log10(x)) - 1

    while x:
        if (new + 1 > 2 ** 31 and sign == 1) or (new > 2 ** 31 and sign == -1):
            return 0
        
        new += (x % 10) * 10 ** i
        i -= 1
        x //= 10

    return new * sign


print('\n', reverseInteger(7))
print('\n', reverseInteger(20))
print('\n', reverseInteger(30))
print(reverseInteger(123))
print(reverseInteger(-123))
print(reverseInteger(120))
print(reverseInteger(2 ** 31 + 1))
print(reverseInteger(0))