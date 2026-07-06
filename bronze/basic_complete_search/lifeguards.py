n = int(input())
t = []
for i in range(n):
  start, end = map(int, input().split())
  t.append((start,end))

max_covered = 0
for fired in range(n):
  covered = set()
  for i in range(n):
    if i != fired:
      start, end = t[i]
      covered.update(range(start, end))
  current = len(covered)
  if current > max_covered:
   max_covered = current

print(max_covered)