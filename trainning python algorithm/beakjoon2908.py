
a, b = (int(''.join(reversed(num))) for num in input().split())

if(a > b):
    print(a)
else:
    print(b)