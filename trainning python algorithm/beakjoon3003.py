
a = list(map(int, input().split()))

c = [1, 1, 2, 2, 2, 8]

rs = [c[i] - a[i] for i in range(6)]

print(' '.join(map(str, rs)))