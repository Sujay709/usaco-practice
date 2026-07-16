N = int(input())
for i in range(N):
    n, m = [int(i) for i in input().split()]
    players = [[int(i) for i in input().split()] for i in range(n)]
    total = 0
    for i in range(n-1):
        for x in range(i+1, n):
            for j in range(m):
                total += abs(players[i][j]-players[x][j])
    print(total)