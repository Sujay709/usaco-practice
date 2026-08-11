n = int(input())
a = list(input())
b = list(input())

count = 0
prev_diff = False

for i in range(n):
  diff = (a[i] != b[i])
  if diff and not prev_diff:
    count += 1
  prev_diff = diff

print(count)