n = int(input())
cow_heights = []
for _ in range(n):
  cow_height = int(input())
  cow_height.append(cow_heights)

sorted_heights = sorted(cow_heights)

count = 0
for i in range(n):
  if cow_heights[i] != sorted_heights[i]:
    count += 1 
print(count - 1)

# ez