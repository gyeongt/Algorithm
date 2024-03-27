import sys

a, b = map(int, sys.stdin.readline().split())

c, d = map(int, sys.stdin.readline().split())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

abGcd = gcd(a, b)
cdGcd = gcd(c, d)

numerator1 = a // abGcd
denominator1 = b // abGcd

numerator2 = c // cdGcd
denominator2 = d // cdGcd

numerator = denominator1 * numerator2 + denominator2 * numerator1
denominator = denominator1 * denominator2

rs = gcd(numerator, denominator)
numerator = numerator // rs
denominator = denominator // rs

print(numerator, denominator)
