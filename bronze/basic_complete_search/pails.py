x, y, m = map(int, input().split())
max_milk = 0
for i in range(((m//x) + 1)):
  for j in range(((m//y) + 1)):
    current_milk = (i*x) + (j*y)
    if current_milk <= m and current_milk > max_milk:
      max_milk = current_milk

print(max_milk)