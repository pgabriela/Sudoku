from random import randint
from random import shuffle
import time
from BacktrackAlgo import backtrackAlg


INIT_NUM = 24


def makeSudoku():
    items = []
    for i in range(1, 10):
        for j in range(1, 10):
            items.append(i)

    shuffle(items)

    sudoku = []
    for i in range(9):
        sudoku.append([])
        for j in range(9):
            sudoku[i].append(0)
    for i in range(INIT_NUM):
        while(1):
            rand1 = randint(0, 8)
            rand2 = randint(0, 8)
            if sudoku[rand1][rand2] == 0:
                sudoku[rand1][rand2] = items.pop()
                break
    return sudoku


def checkSudoku(check):
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if check[i][j] == check[i][k] and j != k and check[i][j] != 0:
                    return False
                if check[i][j] == check[k][j] and i != k and check[i][j] != 0:
                    return False
                if check[((i//3)*3)+(k//3)][((j//3)*3)+(k % 3)] == check[i][j] \
                   and not(((i//3)*3)+(k//3) == i and ((j//3)*3)+(k % 3) == j) \
                   and check[i][j] != 0:
                    return False
    count = 0
    DEGREE_FIRST_ROW = 3
    DEGREE_ALL = 2
    for i in range(9):
        if check[0][i] != 0:
            count += 1
    if count < DEGREE_FIRST_ROW:
        return False
    for i in range(5):
        counter = 0
        for j in range(9):
            if check[i][j] != 0:
                counter += 1
        if counter < DEGREE_ALL:
            return False
    return True


def sudokuGenerator():
    start_time = time.time()
    starting_time = time.time()
    while(1):
        sudoku = makeSudoku()
        flag = checkSudoku(sudoku)
        if(flag):
            print("Generated a sudoku in %s seconds" %
                  (time.time() - start_time))
            print("In progress solving the sudoku")
            startSolving = time.time()
            if(backtrackAlg(sudoku)):
                print("Solved the sudoku in %s seconds" %
                      (time.time() - startSolving))
                break
            else:
                print("This sudoku has no solution (in %s seconds)" %
                      (time.time() - startSolving))
                start_time = time.time()
                continue
    print("--- Successfully generated a sudoku solution in %s seconds ---" %
          (time.time() - starting_time))
    print('\n')
