

n = int(input())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcd(a, b):
    return a * b // gcd(a, b)

for _ in range(n):
    a, b = map(int, input().split())
    print(lcd(a, b))