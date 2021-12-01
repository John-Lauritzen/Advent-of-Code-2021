
depth = [199,
200,
208,
210,
200,
207,
240,
269,
260,
263]

decreases = 0

for i in range(len(depth)):
    if i == 0:
        decreases = 0
    else:
        if depth[i] > depth[i-1]:
            decreases += 1

print(decreases)
