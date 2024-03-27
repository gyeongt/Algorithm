def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n = int(input())
numbers = [int(input()) for _ in range(n)]

numbers.sort()
rs = numbers[1] - numbers[0]
for i in range(1, n - 1):
    rs = gcd(rs, numbers[i+1] - numbers[i])
    
divisor = set()
for i in range(1, int(rs**0.5) + 1):
    if rs % i == 0:
        divisor.add(i)
        divisor.add(rs // i)
divisor.discard(1)

print(" ".join(map(str, sorted(divisor))))

