
a, b, c = map(int, input().split())

if(a == b == c):
    rs = 10000 + a * 1000
    print(rs)
elif(a == b):
    rs = 1000 + a * 100
    print(rs)
elif(a == c):
    rs = 1000 + a * 100
    print(rs)
elif(b == c):
    rs = 1000 + b * 100
    print(rs)
else:   
    rs= max(a, b, c) * 100
    print(rs)