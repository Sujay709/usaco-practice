n, m = map(int, input().split())
speed_limits = []
bessie_speeds =[]
max_infraction = 0

for _ in range(n):
  length, speed = map(int, input().split())
  for _ in range(length):
    speed_limits.append(speed)

for _ in range(m):
  length, speed = map(int, input().split())
  for _ in range(length):
    bessie_speeds.append(speed)

for x in range(100):
  current_infraction = bessie_speeds[x] - speed_limits[x]

  if current_infraction > max_infraction:
    max_infraction = current_infraction

print(max_infraction)