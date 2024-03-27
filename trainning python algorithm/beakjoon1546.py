import sys

n = int(sys.stdin.readline())

testNum = list(map(int, sys.stdin.readline().split()))

rs = [(num/max(testNum)) * 100 for num  in testNum]
    
average = sum(rs) / n
print(average)

 
    