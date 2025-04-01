def roman_to_int(s: str) -> int:
    d = {'I' : 1,
         'V': 5,
         'X': 10,
         'L': 50,
         'C': 100,
         'D': 500,
         'M': 1000}
    
    c = d[s[0]]
    i = 1
    while i < len(s):
        if d[s[i]] > d[s[i - 1]]:
            c += d[s[i]] - 2*d[s[i - 1]]
        else:
            c += d[s[i]]
        i += 1

    return c
    

print(roman_to_int('III'))
