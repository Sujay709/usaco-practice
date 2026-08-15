n = int(input())
grid = []
for i in range(n):
  line= input()
  grid.append([int(char) for char in line])

result = 0
for i in range(n -1, -1, -1):
  for j in range(n -1, -1, -1):
    if grid[i][j] == 1:
      result += 1
      for row in range(i+1):
        for col in range(j +1):
          grid[row][col] = 1 - grid[row][col]
print(result)