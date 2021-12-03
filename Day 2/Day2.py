f = open("cori.txt", "r")
# Convert content to list
lines=f.readlines()

depth = 0
horizontal = 0

#for i in range (len(lines)):
for line in lines:
    text = line.split(" ")
    if (text[0] == "forward"):
        horizontal+= int(text[1])
    if (text[0] == "up"):
        depth -= int(text[1])
    if (text[0] == "down"):
        depth += int(text[1])

print("Contador de altura")
print(depth)
print("Contador horizontal")
print(horizontal)
print("multiplicacion:")
print(depth*horizontal)

input()