
a, b = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcd(a, b):
    return a * b // gcd(a, b)

print(lcd(a, b))