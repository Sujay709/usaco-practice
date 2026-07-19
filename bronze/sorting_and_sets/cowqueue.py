n = int(input())
cows = []

for _ in range(n):
  arrive, dur = map(int, input().split())
  cows.append((arrive, dur))

cows.sort()
current_time = 0
for arrive, dur in cows:
  start = max(current_time, arrive)
  current_time = start + dur

print(current_time)