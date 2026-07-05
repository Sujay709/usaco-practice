n,k = map(int, input().split())
sizes = []
for _ in range(n):
  sizes.append(int(input()))
  sizes.sort

max_diamonds = 0
for i in range(n):
  current_count = 0
  for j in range(i,n):
    if sizes[j] - sizes[i] <= k:
      current_count += 1
    else:
      break
  if current_count > max_diamonds:
    max_diamonds = current_count
print(max_diamonds)
