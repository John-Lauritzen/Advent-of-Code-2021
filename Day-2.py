#day2data = open("Day2-Input.txt", "r")
data = ['forward 5','down 5','forward 8','up 3','down 8','forward 2']
direction = []
distance = []
#for line in day2data:
for line in data:
    value = line.split(' ')
    tempdirection = value[0]
    tempdistance = int(value[1])
    direction.append(tempdirection)
    distance.append(tempdistance)

#day2data.close()



def calcmovement(directlist, distlist):
    depth = 0
    horizontal = 0
    for i in range(len(directlist)):
        if directlist[i] == 'forward':
            horizontal += distlist[i]
        elif directlist[i] == 'down':
            depth += distlist[i]
        else:
            depth -= distlist[i]
    print("Horizontal is:", horizontal, 'Depth is:', depth, 'Product is:', horizontal * depth)


calcmovement(direction, distance)