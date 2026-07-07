n = int(input())
max_area = 0
coordinates = []
for _ in range(n):
  coordinates.append(list(map(int, input().split())))
for i in range(n):
  for j in range(n):
    for k in range(n):
      pt1 = coordinates[i]
      pt2 = coordinates[j]
      pt3 = coordinates[k]
      if pt1[0] == pt2[0] and pt1[1] == pt3[1]:
        base = abs(pt1[0] - pt3[0])
        height = abs(pt1[1] - pt2[1])
        current_area = base * height
        if current_area > max_area:
          max_area = current_area
print(max_area)