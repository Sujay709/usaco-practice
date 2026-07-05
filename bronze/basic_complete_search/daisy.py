n = int(input())
petals = [int(x) for x in input().split()]

average_photos = 0
for i in range(n):
    for j in range(i, n):
        total_petals = 0
        num_flowers = 0
        for k in range(i, j+1):
            total_petals += petals[k]
            num_flowers += 1
            
        # FIXED: These lines must be indented inside the 'j' loop
        if total_petals % num_flowers == 0:
            target_average = total_petals // num_flowers
            has_average_photo = False
            for k in range(i, j+1):
                if petals[k] == target_average:
                    has_average_photo = True
                    break
            if has_average_photo:
                average_photos += 1

print(average_photos)
