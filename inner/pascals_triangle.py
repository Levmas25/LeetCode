'''Given an integer numRows, return the first numRows of Pascal's triangle.'''
def generate(numRows: int) -> list[list[int]]:
    res = []
    for _ in range(numRows):
        res.append([])

    for row in range(numRows):
        for pos in range(row + 1):
            
            if pos == 0:
                res[row].append(1)
                continue

            if pos == row:
                res[row].append(1)
                continue

            res[row].append(res[row - 1][pos - 1] + res[row - 1][pos])

    return res
    

print(*generate(5))
