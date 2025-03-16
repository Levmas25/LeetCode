'''Given a string s, find the length of the longest substring without duplicate characters.'''
def longest_substring(s: str) -> int:
    n = len(s)
    maxLength = 0
    charIndex = [-1] * 128
    left = 0
    
    for right in range(n):
        if charIndex[ord(s[right])] >= left:
            left = charIndex[ord(s[right])] + 1
        charIndex[ord(s[right])] = right
        maxLength = max(maxLength, right - left + 1)
    
    return maxLength


print(longest_substring('dvdf'))