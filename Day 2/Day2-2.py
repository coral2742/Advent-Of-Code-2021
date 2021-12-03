f = open("cori.txt", "r")
# Convert content to list
lines=f.readlines()

depth = 0
horizontal = 0
aim = 0

for line in lines:
    text = line.split(" ")
    if (text[0] == "forward"):
        horizontal += int(text[1])
        depth += (aim * (int(text[1])))
    if (text[0] == "up"):
        aim -= int(text[1])
    if (text[0] == "down"):
        aim += int(text[1])

print("Depth: " + str(depth))
print("Horizontal: " + str(horizontal))
print("Multiplication: " + str(depth*horizontal))
input()