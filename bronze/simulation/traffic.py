n = int(input())
sensors = []

for _ in range(n):
  parts = input().split()
  sensor_type = parts[0]
  low = int(parts[1])
  high = int(parts[2])

  sensors.append((sensor_type, low, high))

start_min = 0
start_max = 1000000000

for i in range(n -1, -1, -1):
  stype, low, high = sensors[i]

  if stype == "none":
    if low > start_min:
      start_min = low
    if high < start_max:
      start_max = high
  elif stype == "off":
    start_min += low
    start_max += high
  elif stype == "on":
    start_min -= high
    start_max -= low
    if start_min < 0:
      start_min =0

print(start_min, start_max)

end_min = start_min
end_max = start_max

for i in range(n):
  stype, low, high = sensors[i]
  if stype == "none":
    if low > end_min:
     end_min = low
    if high < end_max:
      end_max = high
  
  elif stype == "on":
    end_min += low
    end_max += high
  
  elif stype == "off":
    end_min -= high
    end_max -= low
    if end_min < 0:
      end_min = 0

print(end_min, end_max)
  
  
