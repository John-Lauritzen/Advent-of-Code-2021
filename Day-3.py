#testdata = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
values = []

day3data = open("Day3-Input.txt", "r")
for line in day3data:
    temp = line
    values.append(temp.strip())

day3data.close()

def binaryToDecimal(binary):
    
    binary = int(binary)
    decimal = 0
    i = 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

def findCommonBit(data, position):
    countofon = 0
    countofoff = 0
    for i in range(len(data)):
        if data[i][position] == '1':
            countofon += 1
        else:
            countofoff += 1
    if countofon > countofoff:
        return '1'
    elif countofon < countofoff:
        return '0'
    else:
        return 'equal'

def inputtoGammaandEpsilon(data):

    gamma =''
    epsilon = ''

    for pos in range(len(data[0])):
        if findCommonBit(data, pos) == '1':
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    convertedgamma = binaryToDecimal(gamma)
    convertedepsilon = binaryToDecimal(epsilon)

    print('Gamma:', gamma, convertedgamma, 'Epsilon:', epsilon, convertedepsilon, 'Product:', convertedgamma * convertedepsilon)

def oxFilter(data, position):
    combit = findCommonBit(data, position)
    newlist = []
    if combit == 'equal':
        combit = '1'
    for i in range(len(data)):
        if data[i][position] == combit:
            newlist.append(data[i])
    return newlist

def scrubFilter(data, position):
    combit = findCommonBit(data, position)
    newlist = []
    if combit == 'equal':
        combit = '1'
    for i in range(len(data)):
        if data[i][position] != combit:
            newlist.append(data[i])
    return newlist

def inputtoOx(data):
    oxlist = data[:]
    for pos in range(len(data[0])):
        if len(oxlist) != 1:
            templist = oxFilter(oxlist, pos)
            oxlist = templist
    oxvalue = binaryToDecimal(oxlist[0])
    print('Oxygen binary:', oxlist[0], 'Oxygen value:', oxvalue)

def inputtoScrub(data):
    scrublist = data[:]
    for pos in range(len(data[0])):
        if len(scrublist) != 1:
            templist = scrubFilter(scrublist, pos)
            scrublist = templist
    scrubvalue = binaryToDecimal(scrublist[0])
    print('CO2 Scrubber binary:', scrublist[0], 'CO2 Scrubber value:', scrubvalue)

inputtoGammaandEpsilon(values)

inputtoOx(values)
inputtoScrub(values)