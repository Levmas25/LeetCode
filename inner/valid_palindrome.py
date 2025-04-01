import string


def isPalindrome(s: str) -> bool:

        if len(s) == 1 and s.lower() in string.ascii_lowercase:
            return True

        front = 0
        back = len(s) - 1
        allowed = string.ascii_letters + string.digits

        while front < back:

            if s[front].lower() != s[back].lower() and s[front] in allowed and s[back] in allowed:
                return False

            if s[front] not in allowed:
                front += 1
                continue

            if s[back] not in allowed:
                back -= 1
                continue

            front += 1
            back -= 1

isPalindrome("0P")

def solution(s: str) -> bool:
        '''Works a little better'''
        final_string = ("".join(char for char in s if char.isalnum())).lower()
        mid_string = len(final_string)//2
        for i in range(1,mid_string+1):
            if final_string[i-1] != final_string[-i]:
                return False
        return 


def another_sol(s: str) -> bool:
    '''Works much better'''
    filtered_str = ''.join(filter(str.isalnum, str.lower(s)))
    return filtered_str == filtered_str[::-1]