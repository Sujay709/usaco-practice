n = int(input())
statements = []
for i in range(n):
    letter, p = input().split()
    p = int(p)
    statements.append((letter, p))

best = float('inf')

for x in [p for (_, p) in statements]:     
    liars = 0
    for (letter, p) in statements:    
        if letter == 'L':
          if x > p:
            liars += 1
        elif letter == 'G':
          if x < p:
            liars += 1
    best = min(best, liars)
print(best)