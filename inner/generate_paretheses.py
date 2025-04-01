'''Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.'''

def generate_parentheses(n: int) -> str:
    res = ['']*2*n

    cur = 0

