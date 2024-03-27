import sys

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n = int(sys.stdin.readline())

numbers = [int(sys.stdin.readline()) for _ in range(n)]

#간격계산
intervals = []
for i in range(1, len(numbers)):
    interval = numbers[i] - numbers[i - 1]
    intervals.append(interval)

rs = intervals[0]  
for i in range(1, len(intervals)):
    rs = gcd(rs, intervals[i])
    
min_trees = 0
for i in intervals:
    min_trees += i // rs - 1
    
print(min_trees)
    

