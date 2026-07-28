n = int(input())
count = {}
special_pairs = 0

for _ in range(n):
  city, state = input().split()
  city_prefix = city[:2]
  if city_prefix != state:
      target = (state, city_prefix)
      if target in count:
        special_pairs += count[target]
      
      current = (city_prefix, state)
      count[current] = count.get(current, 0) + 1
print(special_pairs)