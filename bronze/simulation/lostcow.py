x, y = map(int,input("").split())
total = 0
reach = 1
direction = 1
location = x

while location != y:
  next_location = x + reach*direction
  if location < y < next_location or next_location < y < location or next_location == y:
    total += abs(y-location)
    print(total)
    break
  else:
    direction = direction * -1
    total += abs(next_location - location)
    location = next_location
    reach *= 2