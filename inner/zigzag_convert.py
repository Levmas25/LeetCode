'''The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:'''
def convert(s: str, numRows: int) -> str:
    '''It`s still good, but could done easier'''
    res = [''] * numRows

    if numRows == 1:
        return s
    
    pos = 0
    ind = 0
    while ind != len(s):
        if pos == numRows:
            pos -= 1
            while pos != 0 and ind < len(s):
                pos -= 1
                res[pos] += s[ind]
                ind += 1
            pos += 1
        
        if ind == len(s):
            break

        res[pos] += s[ind]
        pos += 1
        ind += 1
    
    return ''.join(res)


print(convert("ABCS", 3))

def sol(s: str, numRows: int) -> str:
    '''Works almost twice faster'''
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [""] * numRows  # Create an array of empty strings for each row
    current_row, step = 0, 1  # Start at the first row, moving downward initially

    for char in s:
        rows[current_row] += char  # Append character to the corresponding row

        # Change direction when reaching the top or bottom row
        if current_row == 0:
            step = 1
        elif current_row == numRows - 1:
            step = -1

        current_row += step  # Move up or down

    return "".join(rows)  # Concatenate rows to form the final result