
day1data = open("Day1-1_Input.txt", "r")
depth = []
for line in day1data:
    value = int(line)
    depth.append(value)

day1data.close()

def calcdecrease(depthlist):
    decreases = 0
    for i in range(len(depthlist)):
        if i == 0:
            decreases = 0
        else:
            if depthlist[i] > depthlist[i-1]:
                decreases += 1
    return(decreases)

def slidingcalcdecrease(depthlist2):
    slidingdecreases = 0
    for i in range(len(depthlist2) - 2):
        if i == 0:
            slidingdecreases = 0
        else:
            if (int(depthlist2[i]) + int(depthlist2[i+1]) + int(depthlist2[i+2])) > (int(depthlist2[i-1]) + int(depthlist2[i]) + int(depthlist2[i+1])):
                slidingdecreases += 1
    return(slidingdecreases)


return1 = calcdecrease(depth)
return2 = slidingcalcdecrease(depth)

print("The answer for Part 1 is: ", return1)
print("The answer for Part 2 is: ", return2)