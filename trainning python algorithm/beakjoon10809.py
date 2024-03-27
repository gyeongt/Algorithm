
s = input()

positions = [-1] * 26

for i, char in enumerate(s):
    
    if positions[ord(char) - ord('a')] == -1:
        positions[ord(char) - ord('a')] = i
        
print(' '.join(map(str, positions)))