'''Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
 Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.'''

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    d = {'2': "abc",
         '3': "def",
         '4': "ghi",
         '5': "jkl",
         '6': "mno",
         '7': "pqrs",
         '8': "tuv",
         '9': "wxyz"}
    
    from itertools import product
    strings = []
    for dig in digits:
        if dig == '1':
            continue

        strings.append(d[dig])

    return list(''.join(x) for x in product(*strings))

print(letterCombinations('23'))
print(letterCombinations(''))
print(letterCombinations('2'))