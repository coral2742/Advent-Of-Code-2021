'''
Challenge: https://adventofcode.com/2021/day/4
By Coral Izquierdo Muñiz with ❤️
'''
import re

def win(matrix):
    win = False
    # Iterate looking for winner in a row
    for i in range(0,5):
        rowCounter = 0
        for j in range(0,5):
            # If number is marked with -1, increment rows counter
            if (matrix[i][j] == -1):
                rowCounter = rowCounter + 1
            # Has one complete row
            if (rowCounter == 5):
                return True
    
    # Iterate looking for winner in a column
    for i in range(0,5):
        columnCounter = 0
        for j in range(0,5):
            # If number is marked with -1, increment columns counter
            if (matrix[j][i] == -1):
                columnCounter = columnCounter + 1
            # Has one complete column
            if (columnCounter == 5):
                return True

# In case of winner, calculate points
def getPoints(board, number):
    points = 0
    # Calculate sum of all unmarked numbers
    for i in range(0,5):
        for j in range(0,5):
            if board[i][j] != -1:
                points = points + board[i][j]
    # Multiply for last number
    points = points * number
    return points


points = 0

f = open("cori.txt", "r")
numbers = f.readlines()[0]
# Delete the final \n
numbers = numbers.strip()
numbers = numbers.split(",")
#Convert to int
numbers = list(map(int, numbers))
print(f"Numbers: {numbers}\n")
f.close()

f = open("cori.txt", "r")
parts = f.read().strip().split("\n\n")

# Since line one to last
boards = []
for element in parts[1:]:
    boards.append([])
    for line in element.split('\n'):
        boards[-1].append([int(x) for x in re.findall(r'\d\d?', line)])

print(f"Number of total matrices: {len(boards)}")
# Total number of matrices
total = len(boards)
print(f"Board in pos 0: {boards[0]}")

winner = False
winners = 0
winnersList = []

# Iterate the list of numbers
for number in numbers:
    if winner == True:
        break
    print(f"Number: {number}")
    # Iterate each matrix
    for index, board in enumerate (boards):
        print(f"Matriz {index}: " + str(board))

    # Iterate matrix looking for the number
        # Iterate rows
        for i in range(0,5):
            # Iterate columns
            for j in range(0,5):
                if board[i][j] == number:
                    board[i][j] = -1
        if (win(board)):
            if (index not in winnersList):
                winners = winners + 1
                print(f"Number of winners: {winners}")
                print(f"WINNER: Matrix number {index}")
                print(f"Matrix {index}: " + str(board))
                winnersList.append(index)

        if (winners == total):
            print(f"LAST WINNER: Matrix number {index}")
            print(f"Matrix {index}: " + str(board))
            points = getPoints(board, number)
            print(f"Points: {points}")
            winner = True
            break
                
        print(board)