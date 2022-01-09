'''
Challenge: https://adventofcode.com/2021/day/6
By Coral Izquierdo Muñiz with ❤️
'''
f = open("cori.txt", "r")

initial = f.readlines()[0]
initial = initial.split(",")
# Convert to int list
initial = list(map(int, initial))
print(f"Initial state: {initial}")

# Dictionary with the count of lanternfishes with the internal timer value
fish = {}

# Initialize dictionary
for i in range(9):
    fish.setdefault(str(i),initial.count(i))
print("COUNT")
print(fish)

days = 256

for day in range(days):
    # n will be the number of lanternfishes with an internal time value of zero
    n = fish.get(str(0))

    # After a day, this number of lanternfishes update to the previous day
    for i in range(1, len(fish)):
        fish[str(i - 1)] = fish[str(i)]

    # The number of lanternfishes that have created a new lanternfish (life to 6) will be the same added to the number of new lanternfish created
    fish[str(6)] = fish[str(6)] + n
    # New lanternfishes whit life to 8
    fish[str(8)] = n

total = 0
for number in fish.values():
    total = total + number

print(f"After 256 days, there are a total of {total} fish")
