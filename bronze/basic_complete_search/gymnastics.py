k, n = map(int, input().split())
pos = []
for i in range(k):
  ratings = list(map(int, input().split()))
  rank = [0] * (n+1)
  for j in range(n):
    cow = ratings[j]
    rank[cow] = j
  pos.append(rank)
count = 0
for a in range(1,n+1):
    for b in range(a + 1, n+1):
      a_better = all(pos[s][a] < pos[s][b] for s in range(k))
      b_better = all(pos[s][b] < pos[s][a] for s in range(k))
      if b_better or a_better:
        count+= 1
print(count)
    
