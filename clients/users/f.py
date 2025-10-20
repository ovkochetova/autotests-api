from functools import lru_cache

@lru_cache
def plus(a ,  b):
    print(f" a : {a} + b: {b}")
    return a + b

plus(1, 2)
plus(1, 2)
plus(1, 2)
plus(2, 2)
plus(2, 2)