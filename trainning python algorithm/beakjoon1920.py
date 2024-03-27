import sys
a = int(sys.stdin.readline())
b = set(map(int, sys.stdin.readline().split()))

c = int(sys.stdin.readline())
d = [int(x) for x in sys.stdin.readline().split()]

for i in range(c):         
    if d[i] in b:
        print(1)
    else:
        print(0)