def backtrackAlg(sudoku):
    freeCells = []
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                freeCells.append([i, j])
    stack = []
    if(not recurse(sudoku, freeCells, stack)):
        return False
    else:
        return True


def recurse(sudoku, freeCells, stack):
    for i in range(1, 10):
        stack.append(i)
        sudoku[freeCells[len(stack)-1][0]][freeCells[len(stack)-1][1]] = \
            stack[-1]
        flag = 1
        for x in range(9):
            if sudoku[freeCells[len(stack)-1][0]][x] == stack[-1] and \
               x != freeCells[len(stack)-1][1]:
                flag = 0
                break
            if sudoku[x][freeCells[len(stack)-1][1]] == stack[-1] and \
               x != freeCells[len(stack)-1][0]:
                flag = 0
                break
            if sudoku[((freeCells[len(stack)-1][0]//3)*3)
                      + (x // 3)][((freeCells[len(stack)-1][1]//3)
                                   * 3)+(x % 3)] == stack[-1] \
               and not(
                ((freeCells[len(stack)-1][0]//3)*3)+(x//3) ==
                   freeCells[len(stack)-1][0] and
                ((freeCells[len(stack)-1][1]//3)
                 * 3)+(x % 3) == freeCells[len(stack)-1][1]):
                flag = 0
                break
        if i == 9 and flag == 0:
            sudoku[freeCells[len(stack)-1][0]][freeCells[len(stack)-1][1]] = 0
            stack.pop()
            return False
        if flag == 0:
            sudoku[freeCells[len(stack)-1][0]][freeCells[len(stack)-1][1]] = 0
            stack.pop()
            continue
        else:
            if len(stack) == len(freeCells):
                with open("sud", 'a') as output:
                    for a in range(9):
                        for b in range(9):
                            if b == 8:
                                output.write(str(sudoku[a][b])+'\n')
                            else:
                                output.write(str(sudoku[a][b])+' ')
                    output.write('\n')
                output.close()

                return True
            if recurse(sudoku, freeCells, stack):
                return True
            else:
                sudoku[freeCells[len(stack)-1][0]][freeCells[len(stack)-1][1]]\
                    = 0
                stack.pop()
                if i == 9:
                    return False
                continue
