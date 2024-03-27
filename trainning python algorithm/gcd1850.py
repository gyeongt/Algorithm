import sys

a, b = map(int, sys.stdin.readline().split())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

rs = "1" * gcd(a, b)

print(rs)