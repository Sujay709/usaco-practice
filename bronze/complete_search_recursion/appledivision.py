n = int(input())
p = list(map(int, input().split()))

def solve(i: int, sum1: int, sum2: int):
  if i == n:
    return abs(sum2-sum1)

  return min(
      solve(i + 1, sum1 + p[i], sum2),
      solve(i + 1, sum1, sum2 + p[i])
    )

print(solve(0, 0, 0))