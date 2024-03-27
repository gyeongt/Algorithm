import sys

n = int(sys.stdin.readline())

def gcd(a, b):
    if 0 == b:
        return a
    return gcd(b, a % b)

def sum_gcd(a):
    rs = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            rs += gcd(a[i], a[j])
    return rs
    

for i in range(n):
    a = list(map(int, sys.stdin.readline().split()[1:]))
    print(sum_gcd(a))