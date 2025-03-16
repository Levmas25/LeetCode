'''Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.'''
def convertToTitle(columnNumber: int) -> str:
    res = ""

    while columnNumber > 0:
        columnNumber -= 1
        res = chr((columnNumber % 26) + ord("A")) + res
        columnNumber //= 26
    
    return res


convertToTitle(701)


'''Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.'''
def titleToNumber(columnTitle: str) -> int:
    res = 0

    for i in range(len(columnTitle) - 1, -1, -1):
        res += (ord(columnTitle[i]) - ord('A') + 1) * 26**(len(columnTitle) - i - 1)

    return res


titleToNumber('A')