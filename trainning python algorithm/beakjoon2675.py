

s = int(input())

for _ in range(s):
    r, p = input().split()
    r = int(r)
    
    rs = ""
    
    for i in p:
        rs += i * r
        
    print(rs)
    
    
    