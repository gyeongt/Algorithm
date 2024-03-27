

n, m = map(int, input().split())

basket = [0] * (n + 1)

for _ in range(m):
    i, j, k = map(int, input().split())
    for index in range(i, j + 1):
        basket[index] = k
        
print(" ".join(map(str, basket[1:])))
