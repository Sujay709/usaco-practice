import itertools

cows = sorted(["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"])
n = int(input())
constraint = []
for _ in range(n):
  parts = input().split()
  x, y = parts[0], parts[-1]
  constraint.append((x,y))

for perm in itertools.permutations(cows):
  valid = True
  for x, y in constraint:
    if abs(perm.index(x) - perm.index(y)) != 1:
      valid = False
      break
  if valid:
    for cow in perm:
      print(cow)
    break