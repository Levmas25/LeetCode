print("A \tB\tF")

for A in 0, 1:
    for B in 0, 1:
        F = (not(A^B)) and ((not A) + (not B))
        print(f'{A}\t{B}\t{int(F)}')