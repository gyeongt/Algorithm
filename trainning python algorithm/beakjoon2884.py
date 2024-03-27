

h, m = map(int, input().split())

if(m < 45):
    h = h - 1 if h > 0 else 23
    m = 60 - (45 - m)
else:
    m = m - 45
    
print(h, m)