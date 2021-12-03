#data = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
values = []

day3data = open("Day3-Input.txt", "r")
for line in day3data:
    temp = line
    values.append(temp.strip())

day3data.close()

def binaryToDecimal(binary):
    
    binary = int(binary)
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

def inputtoGammaandEpsilon(data):

    gamma =''
    epsilon = ''

    for pos in range(len(data[0])):
        countofon = 0
        total = 0
        for i in range(len(data)):
            if data[i][pos] == '1':
                countofon += 1
            total += 1
        if countofon > (total//2):
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    convertedgamma = binaryToDecimal(gamma)
    convertedepsilon = binaryToDecimal(epsilon)

    print('Gamma:', gamma, convertedgamma, 'Epsilon:', epsilon, convertedepsilon, 'Product:', convertedgamma * convertedepsilon)

inputtoGammaandEpsilon(values)