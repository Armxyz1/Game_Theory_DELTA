# PSEUDOCODE
# /*******
#  * for Tic-Tac-Toe, make an array for the 3D space
#  * take inputs
#  *
#  * recursive call
#  * check whose turn
#  *
#  * if PLAYER's turn then place its symbol at each empty space
#  * if only one was empty then check if PLAYER is winning
#  * if yes then return -inf
#  * if not then return 0
#  * if more than one was empty then place a symbol wherever result is -inf
#  *
#  * if COMPUTER's turn then place its symbol at each empty space
#  * if only one was empty then check if COMPUTER is winning
#  * if yes then return +inf
#  * if not then return 0
#  * if more than one was empty then place a symbol wherever result is +inf
#  *
#  */


"""



















"""


# getIndex function
def getIndex(rowNum, colNum):
    return ((rowNum - 1) * 3) + (colNum - 1)


# getRowCol function
def getRowCol(index):
    r = int((index / 3)) + 1
    c = index - ((r - 1) * 3) + 1
    r = str(r)
    c = str(c)
    retString = r + " " + c

    return retString


"""
















"""


# winnerCheck function
def winnerCheck(grid, symbol):
    # checking for diagonal
    if (
        grid[getIndex(2, 2)] == symbol
        and grid[getIndex(1, 1)] == symbol
        and grid[getIndex(3, 3)] == symbol
    ):
        return 1
    elif (
        grid[getIndex(2, 2)] == symbol
        and grid[getIndex(1, 3)] == symbol
        and grid[getIndex(3, 1)] == symbol
    ):
        return 1

    # checking for horizontals
    if (
        grid[getIndex(1, 1)] == symbol
        and grid[getIndex(1, 2)] == symbol
        and grid[getIndex(1, 3)] == symbol
    ):
        return 1
    elif (
        grid[getIndex(2, 1)] == symbol
        and grid[getIndex(2, 2)] == symbol
        and grid[getIndex(2, 3)] == symbol
    ):
        return 1
    elif (
        grid[getIndex(3, 1)] == symbol
        and grid[getIndex(3, 2)] == symbol
        and grid[getIndex(3, 3)] == symbol
    ):
        return 1

    # checking for verticals
    if (
        grid[getIndex(1, 1)] == symbol
        and grid[getIndex(2, 1)] == symbol
        and grid[getIndex(3, 1)] == symbol
    ):
        return 1
    elif (
        grid[getIndex(1, 2)] == symbol
        and grid[getIndex(2, 2)] == symbol
        and grid[getIndex(3, 2)] == symbol
    ):
        return 1
    elif (
        grid[getIndex(1, 3)] == symbol
        and grid[getIndex(2, 3)] == symbol
        and grid[getIndex(3, 3)] == symbol
    ):
        return 1

    # final return in case of NONE OF ABOVE
    return 0


"""


























"""


# planMove function
def planMove(grid, turn, numTurns):
    # computer's turn
    if turn == 1:
        # base case
        if numTurns == 8:
            # creating return dictionary
            outcomes = dict()

            # putting at empty place
            x = 0
            for y in range(9):
                if grid[y] == " ":
                    grid[y] = "0"
                    x = y
                    break

            # checking the winner
            if winnerCheck(grid, "0") == 1:
                outcomes.update({x: [1, 0, 0]})
            elif winnerCheck(grid, "*") == 1:
                outcomes.update({x: [0, 1, 0]})
            else:
                outcomes.update({x: [0, 0, 1]})

            # setting things back
            grid[x] = " "

            # returning the dictionary
            return outcomes

        # else case
        else:
            # creating return dictionary
            outcomes = dict()

            # run through all the possible combinations
            for x in range(9):
                if grid[x] == " ":
                    grid[x] = "0"

                    # checking if win created
                    if winnerCheck(grid, "0") == 1:
                        outcomes.update({x: [1, 0, 0]})
                    elif winnerCheck(grid, "*") == 1:
                        outcomes.update({x: [0, 1, 0]})
                    else:
                        # moving on
                        ele = planMove(grid, 0, numTurns + 1)

                        # updating in the final values
                        WINS = 0
                        LOSES = 0
                        DRAWS = 0
                        for e in ele:
                            WINS += ele.get(e)[0]
                            LOSES += ele.get(e)[1]
                            DRAWS += ele.get(e)[2]

                        # updating in the outcomes dictionary
                        outcomes.update({x: [WINS, LOSES, DRAWS]})

                    # setting things back
                    grid[x] = " "

            # returning the outcomes
            return outcomes

    # player's turn
    if turn == 0:
        # base case
        if numTurns == 8:
            # creating return dictionary
            outcomes = dict()

            # putting at empty place
            x = 0
            for y in range(9):
                if grid[y] == " ":
                    grid[y] = "*"
                    x = y
                    break

            # checking the winner
            if winnerCheck(grid, "0") == 1:
                outcomes.update({x: [1, 0, 0]})
            elif winnerCheck(grid, "*") == 1:
                outcomes.update({x: [0, 1, 0]})
            else:
                outcomes.update({x: [0, 0, 1]})

            # setting things back
            grid[x] = " "

            # returning the dictionary
            return outcomes

        # else case
        else:
            # creating return dictionary
            outcomes = dict()

            # run through all the possible combinations
            for x in range(9):
                if grid[x] == " ":
                    grid[x] = "*"

                    # checking if win created
                    if winnerCheck(grid, "0") == 1:
                        outcomes.update({x: [1, 0, 0]})
                    elif winnerCheck(grid, "*") == 1:
                        outcomes.update({x: [0, 1, 0]})
                    else:
                        # moving on
                        ele = planMove(grid, 1, numTurns + 1)

                        # updating in the final values
                        WINS = 0
                        LOSES = 0
                        DRAWS = 0
                        for e in ele:
                            WINS += ele.get(e)[0]
                            LOSES += ele.get(e)[1]
                            DRAWS += ele.get(e)[2]

                        # updating in the outcomes dictionary
                        outcomes.update({x: [WINS, LOSES, DRAWS]})

                    # setting things back
                    grid[x] = " "

            # returning the outcomes
            return outcomes


"""


















"""


# makeMove function
def makeMove(grid, turn, numTurns):
    # planning the next move
    result = planMove(grid, turn, numTurns)
    retString = ""

    # checking for any CLEAR WINS
    clearWin = 0
    for all in result:
        if (
            result.get(all)[0] == 1
            and result.get(all)[1] == 0
            and result.get(all)[2] == 0
        ):
            retString = getRowCol(all)
            clearWin = 1
            break

    if clearWin == 0:
        # checking for any CLEAR LOSES
        clearLoss = 0
        for x in range(9):
            if grid[x] == " ":
                grid[x] = "*"
                if winnerCheck(grid, "*") == 1:
                    retString = getRowCol(x)
                    clearLoss = 1
                    grid[x] = " "
                    break
                grid[x] = " "

    if clearWin == 0 and clearLoss == 0:
        # otherwise minimizing loses and maximizing wins
        minLoses = 100000000
        maxWins = -1
        maxDraws = -1
        winIndex = -1
        for all in result:
            if result.get(all)[2] < minLoses:
                minLoses = result.get(all)[2]
                winIndex = all
            elif result.get(all)[2] == minLoses:
                if result.get(all)[0] > maxWins:
                    maxWins = result.get(all)[0]
                    winIndex = all
                elif result.get(all)[0] == maxWins:
                    if result.get(all)[1] > maxDraws:
                        maxDraws = result.get(all)[1]
                        winIndex = all

        # getting the return string
        retString = getRowCol(winIndex)

    # returning value
    return retString


"""




















"""


# displayGrid function
def displayGrid(grid):
    print("-------")
    print("|" + grid[0] + "|" + grid[1] + "|" + grid[2] + "|")
    print("|" + grid[3] + "|" + grid[4] + "|" + grid[5] + "|")
    print("|" + grid[6] + "|" + grid[7] + "|" + grid[8] + "|")
    print("-------")
    print("This is the current grid!\n")


"""















"""


# main function
def main():
    # taking input of player name
    Player = input("Enter your player name: ")
    print("\nWelcome {}!".format(Player))

    # making a grid list
    grid = list()

    # initializing arr
    for i in range(9):
        grid.append(" ")

    # displaying the initial grid
    print("Let's BEGIN!!\n")

    # loop till winner not found
    turn = 0
    numTurns = 0
    while numTurns != 9 and winnerCheck(grid, "*") == 0 and winnerCheck(grid, "0") == 0:
        # player's turn
        if turn == 0:
            displayGrid(grid)
            print("{}'s turn".format(Player))
            r, c = input("Enter row & column number of your next move : ").split(" ")
            r = int(r)
            c = int(c)
            print("\n\n")

            # updating the grid after turn
            grid[getIndex(r, c)] = "*"

            # updating other values
            turn = 1
            numTurns += 1

        # computer's turn
        elif turn == 1:
            print("Computer's turn")
            print("\n\n")
            r, c = makeMove(grid, turn, numTurns).split(" ")
            r = int(r)
            c = int(c)

            # updating the grid after turn
            grid[getIndex(r, c)] = "0"

            # updating other values
            turn = 0
            numTurns += 1

    # printing the WINNER
    if winnerCheck(grid, "*") == 1:
        displayGrid(grid)
        print("{} WINS! Congratulations!!".format(Player))

    elif winnerCheck(grid, "0") == 1:
        displayGrid(grid)
        print("Computer WINS!")

    else:
        displayGrid(grid)
        print("It's a DRAW! Well played!")

    return 1


"""
















"""

# calling the main function
main()
