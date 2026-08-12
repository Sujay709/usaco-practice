n, k = map(int, input().split())
d = list(map(int, input().split()))
result = k + 1
for i in range(1,n):
  result += min(d[i] - d[i - 1], k+1)

print(result)