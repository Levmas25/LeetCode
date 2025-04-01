'''You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.'''
def plus_one(digits: list[int]) -> list[int]:
    i = len(digits) - 1
    to_add = 1

    while to_add != 0:
        if i == 0 and to_add == 1 and digits[i] == 9:
            digits[0] = 1
            digits.append(0)
            break
        digits[i] = (digits[i] + to_add) % 10
        to_add = digits[i] == 0
        i -= 1

    return digits

print(plus_one([9, 9, 9, 9]))
