x = list(map(int, input().split()))
x.sort()
g1 = x[1] - x[0]
g2 = x[2] - x[1]

if g1 == 1 and g2 == 1:
  min_moves = 0
elif g1 <= 2 or g2 <=2:
  min_moves = 1
else:
  min_moves = 2

max_moves = max(g1-1, g2-1)

print(min_moves)
print(max_moves)