from random import randint

EASY_BLANK = 30
MODERATE_BLANK = 45
HARD_BLANK = 65
ONE_SUDOKU = 163
sudoku = []

# Fetching a sudoku solution
with open("sud", "a+") as sud:
    total = sud.tell()
    num = total / ONE_SUDOKU
    rand1 = randint(0, num)
    sud.seek(rand1*ONE_SUDOKU, 0)
    for i in range(9):
        sudoku.append(sud.readline().rstrip().split(' '))

# Writing the solutions
with open("./easy/easySolution", "a+") as easySolution:
    with open("./hard/hardSolution", "a+") as hardSolution:
        with open("./moderate/moderateSolution", "a+") as moderateSolution:
            for i in range(9):
                for j in range(9):
                    if j == 8:
                        easySolution.write(str(sudoku[i][j])+"\n")
                        hardSolution.write(str(sudoku[i][j])+"\n")
                        moderateSolution.write(str(sudoku[i][j])+"\n")
                    else:
                        easySolution.write(str(sudoku[i][j])+" ")
                        hardSolution.write(str(sudoku[i][j])+" ")
                        moderateSolution.write(str(sudoku[i][j])+" ")
            easySolution.write("\n")
            hardSolution.write("\n")
            moderateSolution.write("\n")


# For the easy one
with open("./easy/easy", "a+") as easy:
    sudokuEasy = []
    for i in range(9):
        sudokuEasy.append([])
        for j in range(9):
            sudokuEasy[i].append(sudoku[i][j])

    counter = 0
    while(counter < EASY_BLANK):
        randRow = randint(0, 8)
        randCol = randint(0, 8)
        if sudokuEasy[randRow][randCol] == 0:
            continue
        else:
            sudokuEasy[randRow][randCol] = 0
            counter += 1

    for i in range(9):
        for j in range(9):
            if j == 8:
                easy.write(str(sudokuEasy[i][j])+"\n")
            else:
                easy.write(str(sudokuEasy[i][j])+" ")
    easy.write("\n")


# For the moderate one
with open("./moderate/moderate", "a+") as moderate:
    sudokuModerate = []
    for i in range(9):
        sudokuModerate.append([])
        for j in range(9):
            sudokuModerate[i].append(sudoku[i][j])

    counter = 0
    while(counter < MODERATE_BLANK):
        randRow = randint(0, 8)
        randCol = randint(0, 8)
        if sudokuModerate[randRow][randCol] == 0:
            continue
        else:
            sudokuModerate[randRow][randCol] = 0
            counter += 1

    for i in range(9):
        for j in range(9):
            if j == 8:
                moderate.write(str(sudokuModerate[i][j])+"\n")
            else:
                moderate.write(str(sudokuModerate[i][j])+" ")
    moderate.write("\n")


# For the hard one
with open("./hard/hard", "a+") as hard:
    sudokuHard = []
    for i in range(9):
        sudokuHard.append([])
        for j in range(9):
            sudokuHard[i].append(sudoku[i][j])

    notZero = []
    for i in range(9):
        for j in range(9):
            notZero.append([i, j])

    counter = 0
    while(counter < HARD_BLANK):
        randRowCol = randint(0, len(notZero) - 1)
        if sudokuHard[notZero[randRowCol][0]][notZero[randRowCol][1]] == 0:
            notZero.remove(notZero[randRowCol])
            continue
        else:
            sudokuHard[randRow][randCol] = 0
            notZero.remove(notZero[randRowCol])
            counter += 1

    for i in range(9):
        for j in range(9):
            if j == 8:
                hard.write(str(sudokuHard[i][j])+"\n")
            else:
                hard.write(str(sudokuHard[i][j])+" ")
    hard.write("\n")
