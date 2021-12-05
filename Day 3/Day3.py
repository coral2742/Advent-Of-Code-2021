'''
Challenge: https://adventofcode.com/2021/day/3
By Coral Izquierdo Muñiz with ❤️
'''
contadorCeros = 0
contadorUnos = 0

gamma = ""
epsilon = ""

f = open("cori.txt", "r")
# Convert content to list
lines=f.readlines()

for i in range (0, 12):
    for line in lines:
        if (line[i]) == "1":
            contadorUnos = contadorUnos + 1
        if (line[i] == "0"):
            contadorCeros = contadorCeros + 1

    if (contadorCeros > contadorUnos):
        gamma = gamma + "0"
        epsilon = epsilon + "1"

    else:
        gamma = gamma + "1"
        epsilon = epsilon + "0"

    contadorCeros = 0
    contadorUnos = 0

print("epsilon: " + epsilon)
print("gamma: "+ gamma)

print("Epsilon:" + str(int(epsilon,2)))
print("Gamma: " + str(int(gamma,2)))
        
power = (int(epsilon,2) * int(gamma,2))
print("Power: " + str(power))