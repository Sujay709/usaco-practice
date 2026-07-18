n = int(input()) * 2
weight = list(map(int, input().split()))
weight.sort()
ans = float("inf")
for i in range(len(weight)):
  for j in range(i+1, len(weight)):
    new_weight = []
    for k in range(len(weight)):
      if k != i and k != j:
        new_weight.append(weight[k])
    
    total_instability = 0
    for k in range(0, len(new_weight), 2):
      total_instability += new_weight[k+1] - new_weight[k]
    ans = min(total_instability, ans)
print(ans)