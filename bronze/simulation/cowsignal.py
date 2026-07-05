m,n,k = map(int, input("").split())

for i in range(m):
  row = input()
  expanded_row = ""
  for char in row:
    expanded_row += char * k

  for _ in range(k):
    print(expanded_row)


