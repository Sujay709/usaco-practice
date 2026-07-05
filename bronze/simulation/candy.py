N, M = map(int, input().split())

cows = list(map(int, input().split()))
canes = list(map(int, input().split()))

for cane in canes:
  bottom = 0
  for i in range(N):
    if cows[i] > bottom:
      eaten = min(cows[i], cane) - bottom
      cows[i] += eaten
      bottom += eaten

    if bottom == cane:
      break
for cow in cows:
  print(cow)