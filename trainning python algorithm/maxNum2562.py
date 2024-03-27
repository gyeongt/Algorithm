
num = [int(input()) for _ in range(9)]

maxNum = num[0]

for i in range(1, len(num)):
    if(num[i] > maxNum):
        maxNum = num[i]

print(maxNum)
print(num.index(max(num)) + 1)

# print(max(num))
# print(num.index(max(num)) + 1)




