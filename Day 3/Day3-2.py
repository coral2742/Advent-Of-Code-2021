'''
Challenge: https://adventofcode.com/2021/day/3
By Coral Izquierdo Muñiz with ❤️
'''
def getGamma(list, pos):
    zeros = 0
    ones = 0

    for line in list:
        if line[pos] == "1":
            ones = ones + 1
        else:
            zeros = zeros + 1
    
    if (zeros > ones):
        return "0"
    else:
        return "1"

def getEpsilon(list, pos):
    zeros = 0
    ones = 0

    for line in list:
        if line[pos] == "1":
            ones = ones + 1
        else:
            zeros = zeros + 1
    
    if (zeros > ones):
        return "1"
    else:
        return "0"

def getOxygen(list, pos):
    num = getGamma(list, pos)
    if (len(list) == 1):
        return list
    result = []
    for each in list:
        if each[pos] == num:
            result.append(each)
    return getOxygen(result, pos+1)

def getCO2(list, pos):
    num = getEpsilon(list, pos)
    if (len(list) == 1):
        return list
    result = []
    for each in list:
        if each[pos] == num:
            result.append(each)
    return getCO2(result, pos+1)

f = open("cori.txt", "r")
lines = f.readlines()
oxygen = getOxygen(lines, 0)
print("Oxygen: " + str(int(oxygen[0], 2)))
co2 = getCO2(lines, 0)
print("CO2: " + str(int(co2[0], 2)))
life = int(oxygen[0], 2) * int(co2[0], 2)
print("Life: " + str(life))