

a, b = map(int, input().split())
c = int(input())


b = b + c
if(b >= 60):
    d = b//60
    b = b%60
    a = a + d
    if(a >= 24):
        a= a - 24
        
print(a, b)
