'''
Challenge: https://adventofcode.com/2021/day/6
By Coral Izquierdo Muñiz with ❤️
'''
f = open("cori.txt", "r")

initial = f.readlines()[0]
initial = initial.split(",")
#Convert to int list
initial = list(map(int, initial))
print(f"Initial state: {initial}")

days = 80

while (days > 0):
    fish = len(initial)
    for i in range(fish):
        if (initial[i] == 0):
            initial.append(8)
            initial[i] = 6
        else:
            initial[i] = initial[i] - 1
    days = days - 1

fish = len(initial)

print(f"After 80 days, there are a total of {fish} fish")
