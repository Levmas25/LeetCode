'''You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?'''
from functools import lru_cache
@lru_cache(maxsize=None)
def climbing_stairs(n: int) -> int:
    if n < 0:
        return 0
    if n == 1 or n == 0:
        return 1
    
    return climbing_stairs(n - 1) + climbing_stairs(n - 2)

print(climbing_stairs(4))