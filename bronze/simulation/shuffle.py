SHUFFLE_NUM = 3

with open("shuffle.in") as read:
	n = int(read.readline())
	shuffle = list(map(int, read.readline().split()))
	ids = list(map(int, read.readline().split()))

for _ in range(SHUFFLE_NUM):
	past_order = [0] * n
	for i in range(n):
		# -1 because the shuffle input starts from 1
		past_order[i] = ids[shuffle[i] - 1]
	ids = past_order.copy()

with open("shuffle.out", "w") as written:
	for i in past_order:
		print(i, file=written)
