f = open("cori.txt", "r")
# Convert content to list
lines=f.readlines()   

counter = 0
# Convert str list to int list
for i in range(len(lines)):
    lines[i] = int(lines[i])

for i in range (0, len(lines)-1):
    if ( lines[i+1] > lines[i] ):
        counter += 1

print("Counter: " + str(counter))

input()