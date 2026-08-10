n = int(input())
s = input().strip()

pos = []
for i in range(n):
    if s[i] == "1":
        pos.append(i)
if len(pos) == 0:
    print(n - 1)
else:
    min_d = n
    for i in range(len(pos) - 1):
        dist = pos[i+1] - pos[i]
        if dist < min_d:
            min_d = dist
    
    one_cow = []
    one_cow.append(pos[0]) 
    one_cow.append(n - 1 - pos[-1]) 
    for i in range(len(pos) - 1):
        one_cow.append((pos[i+1] - pos[i]) // 2)
        
    two_cows = []
    two_cows.append(pos[0] // 2) 
    two_cows.append((n - 1 - pos[-1]) // 2) 
    for i in range(len(pos) - 1):
        two_cows.append((pos[i+1] - pos[i]) // 3)
        
    one_cow.sort()
    two_cows.sort()
    
    ans = one_cow[-2] 
    if two_cows[-1] > ans:
        ans = two_cows[-1]
        
    if ans > min_d:
        ans = min_d
        
    print(ans)