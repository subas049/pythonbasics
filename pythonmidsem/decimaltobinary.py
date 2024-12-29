from math import floor


def decimaltobinary(n):
    if n<=1:
        return n
    return str(decimaltobinary(floor(n/2)))+str(n%2)

print(decimaltobinary(21))
