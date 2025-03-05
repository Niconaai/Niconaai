import random as rand

def testRow(arr, rowCheck):
    if((arr[rowCheck-1][0] == "X" and arr[rowCheck-1][1] == "X" and arr[rowCheck-1][2] == "X") or (arr[rowCheck-1][0] == "O" and arr[rowCheck-1][1] == "O" and arr[rowCheck-1][2] == "O")):
        return True
    else:
        return False
    
def testCol(arr, colCheck):
    if((arr[0][colCheck-1] == "X" and arr[1][colCheck-1] == "X" and arr[2][colCheck-1] == "X") or (arr[0][colCheck-1] == "O" and arr[1][colCheck-1] == "O" and arr[2][colCheck-1] == "O")):
        return True
    else:
        return False
    
def testDiag(arr):
    if((arr[0][0] == "X" and arr[1][1] == "X" and arr[2][2] == "X") or (arr[0][0] == "O" and arr[1][1] == "O" and arr[2][2] == "O") or 
       (arr[0][2] == "X" and arr[1][1] == "X" and arr[2][0] == "X") or (arr[0][2] == "O" and arr[1][1] == "O" and arr[2][0] == "O")):
        return True
    else:
        return False

gameOver = True

print("Welcome to TicTacToe")
#username = input("What is your name? ")
print("We shal start...")

array = [
    ['_','_','_'],
    ['_','_','_'],
    ['_','_','_']
]
print("We start fresh: ")
for row in array:
    print(row)
print(" ")

print("You are awarded the first turn, and you will be X...")
print("The game is played by typing the row and the column as your choice")
firstR = 0
firstC = 0
while(firstR >= 4 or firstR <= 0):
    firstR = int(input("Please input your first row selection: "))
while(firstC >= 4 or firstC <= 0):
    firstC = int(input("Please input your first column selection: "))

array[firstR-1][firstC-1] = "X"

randomC = rand.randint(1,3)
randomR = rand.randint(1,3)

while(array[randomR-1][randomC-1] != "_"):
    randomC = rand.randint(1,3)
    randomR = rand.randint(1,3)

print("The computer chose Row " + str(randomR) + " and Col " + str(randomC))

array[randomR-1][randomC-1] = "O"

for row in array:
    print(row)
print(" ")

count = 1

while(gameOver != False):
    count += 1
    print("Turn " + str(count))

    newR = 0
    newC = 0
    while((newR >= 4 or newR <= 0) and (newC >= 4 or newC <= 0) or (array[newR-1][newC-1] != "_")):
        newR = int(input("Please input your row selection: "))
        newC = int(input("Please input your column selection: "))

    array[newR-1][newC-1] = "X"

    newRandomC = rand.randint(1,3)
    newRandomR = rand.randint(1,3)
    while(array[newRandomR-1][newRandomC-1] != "_"):
        newRandomC = rand.randint(1,3)
        newRandomR = rand.randint(1,3)

    print("The computer chose Row " + str(newRandomR) + " and Col " + str(newRandomC))

    array[newRandomR-1][newRandomC-1] = "O"

    for row in array:
        print(row)
    print(" ")

    row1 = False
    row2 = False
    row3 = False
    col1 = False
    col2 = False
    col3 = False
    diag = False

    row1 = testRow(array, 1)
    row2 = testRow(array, 2)
    row3 = testRow(array, 3)
    col1 = testCol(array, 1)
    col2 = testCol(array, 2)
    col3 = testCol(array, 3)
    diag = testDiag(array)

    if(row1 or row2 or row3 or col1 or col2 or col3 or diag):
        gameOver = True
        print("GAME OVER")
        break