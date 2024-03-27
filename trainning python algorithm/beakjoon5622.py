

t = input()

diel = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

rs = 0
for i in t:
    
    for j in diel:
        
        if i in j:
            rs += diel.index(j) + 3
            
print(rs)