# Given an integer x, return true if x is a palindrome, and false otherwise.
def palindrome_number(x: int) -> bool:
    if x < 0:
        return False
    
    s_x = str(x)
    
    left = 0
    right = len(s_x) - 1
    while left < right:
        if s_x[left] != s_x[right]:
            return False
        right -= 1
        left += 1
    
    return True
