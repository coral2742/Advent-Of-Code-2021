'''
Challenge: https://adventofcode.com/2021/day/5
By Coral Izquierdo Muñiz with ❤️
'''
# Calculate the maximum length of the matrix
def getSize():
    f = open("cori.txt", "r")
    size = 0
    for line in f:
        x1 = int(line.strip().split(" -> ")[0].split(",")[0])
        y1 = int(line.strip().split(" -> ")[0].split(",")[1])
        x2 = int(line.strip().split(" -> ")[1].split(",")[0])
        y2 = int(line.strip().split(" -> ")[1].split(",")[1])
        
        size = max(size, x1, x2, y1, y2)
    return size + 1

coords = []
size = getSize()
print(f"SIZE: {size}") 

# Initialize the matrix of coordinates to zero
for x in range(size):
    coords.append([])
    for y in range(size):
        coords[x].append(0)


f = open("cori.txt","r")
for line in f:
    x1 = int(line.strip().split(" -> ")[0].split(",")[0])
    y1 = int(line.strip().split(" -> ")[0].split(",")[1])
    x2 = int(line.strip().split(" -> ")[1].split(",")[0])
    y2 = int(line.strip().split(" -> ")[1].split(",")[1])
    
    maxX = max(x1, x2)
    minX = min(x1, x2)
    maxY = max(y1, y2)
    minY = min(y1, y2)

    # Si 1,5 -> 1,9
    # Horizontal case (x1 == x2)
    if (x1 == x2):
        while minY <= maxY:
            coords[x1][minY] = coords[x1][minY] + 1
            minY = minY + 1        
    
    # Si 1,5 -> 3,5
    # Vertical case (y1 == y2)
    elif (y1 == y2):
        while minX <= maxX:
            coords[minX][y1] = coords[minX][y1] + 1
            minX = minX + 1


    # Diagonal case
    else:
        x = minX
        if (x1 < x2):
            y = y1
        else:
            y = y2

        if (y == minY):
            while ((x <= maxX) and (y <= maxY)):
                coords[x][y] = coords[x][y] + 1
                x = x + 1
                y = y + 1
        else:
            while ((x <= maxX) and (y >= minY)):
                coords[x][y] = coords[x][y] + 1
                x = x + 1
                y = y - 1

  
print(coords)

# Calculate the total number of points with a 2 or larger
points = 0
for i in range(size):
    for j in range(size):
        if (coords[i][j] >= 2 ):
            points = points + 1

print(f"Points with 2 or larger: {points}")
