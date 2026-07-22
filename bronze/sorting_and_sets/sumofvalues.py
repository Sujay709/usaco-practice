n, x = map(int, input().split())
nums = list(map(int, input().split()))
m = {}
for i, a in enumerate(nums):
	if x - a in m:
		print(i + 1, m[x - a] + 1)
		break
	m[a] = i
else:
	print("IMPOSSIBLE")