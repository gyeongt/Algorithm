import sys

remainList = []
for i in range(10):
    n = int(sys.stdin.readline())   

    remainList.append(n%42)
    

print(len(set(remainList)))
    
    