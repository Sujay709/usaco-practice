max_time = 1000

with open("blist.in") as read:
  n = int(read.readline())
  cows = [[int(i) for i in read.readline().split()] for _ in range(n)]

max_buckets = 0
for t in range(1, max_time + 1):
  curr_buckets = 0  
  for c in cows:
    if c[0] <= t <= c[1]:
      curr_buckets = curr_buckets + c[2]
  
  max_buckets = max(max_buckets, curr_buckets)
print(max_buckets, file=open("blist..out", "w"))