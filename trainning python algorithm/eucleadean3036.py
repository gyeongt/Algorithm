
n = int(input())
a = list(map(int, input().split()))
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


for i in range(1, n):
    current_gcd = gcd(a[0], a[i])
    
    print(f"{a[0] // current_gcd}/{a[i] // current_gcd}")
