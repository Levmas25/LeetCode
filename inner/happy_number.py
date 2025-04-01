'''Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.'''
def isHappy(n: int) -> bool:
    new_n = 0
    while True:
        copy = n
        if n == 1 or n == 7:
            return True
        
        if n < 10:
            return False
        
        while copy != 0:
            new_n += (copy % 10) ** 2 
            copy //= 10


        n = new_n
        new_n = 0


isHappy(2)