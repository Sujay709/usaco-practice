n = int(input())
mailbox = input().strip()
for k in range(1,n + 1):
  seen_string = set()
  unique = True
  for i in range(n-k +1):
    current_string = mailbox[i:i+k]
    if current_string in seen_string:
      unique = False
      break
    seen_string.add(current_string)
  if unique:
    print(k)
    break