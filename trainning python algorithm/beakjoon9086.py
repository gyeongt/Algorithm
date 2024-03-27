
n = int(input())

for _ in range(n):
    i = str(input())
    
    print(''.join([i[0], i[-1]]))