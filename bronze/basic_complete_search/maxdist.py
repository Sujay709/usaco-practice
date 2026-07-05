n =  int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

max_sqaured = 0 
for i in range(n):
  for j in range(i+1,n):
    dx = x[i] - x[j]
    dy = y[i] - y[j]
    square = dx * dx + dy*dy
    max_sqaured = max(max_sqaured, square)
print(max_sqaured)
