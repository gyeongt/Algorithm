
n = int(input())
rs = []

def fact(n, rs):
    if(n == 0):
        rs.append(0)
        return
    if(n == 1):
        rs.append(1)
        return
    if(n % 2 == 0):
        rs.append(0)
        fact(n // -2, rs)
    else:
        rs.append(1)
        fact((n // -2) + 1, rs)
        
fact(n, rs)
rs.reverse()
print(f'{"".join(str(i) for i in rs)}')
        