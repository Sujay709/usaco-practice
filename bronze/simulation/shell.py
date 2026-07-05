n = int(input())
swaps = []
for _ in range(n):
    a, b, g = map(int, input().split)
    swaps.append((a, b, g))
best = 0
for start in [1,2,3]:
    pos = start
    score = 0
    for a,b,g in swaps:
        if pos == a:
            pos = b
        elif pos == b:
            pos = a
        elif pos == g:
            score += 1
    if score > best:
        best = score
print(best)