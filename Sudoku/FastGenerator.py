import random
import time

ONE_SUDOKU = 163


def transformer(sudoku):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    pairs = []
    while(len(numbers) >= 2):
        r1 = random.randint(0, len(numbers)-1)
        pairs.append([])
        pairs[-1].append(numbers[r1])
        numbers.pop(r1)
        r2 = random.randint(0, len(numbers)-1)
        pairs[-1].append(numbers[r2])
        numbers.pop(r2)
    for i in pairs:
        temp = []
        for x in range(9):
            for y in range(9):
                if(sudoku[x][y] == i[1]):
                    temp.append([x, y])
        for x in range(9):
            for y in range(9):
                if(sudoku[x][y] == i[0]):
                    sudoku[x][y] = i[1]
        for x in temp:
            sudoku[x[0]][x[1]] = i[0]


while(True):
    transformed = []
    ans = open("sud", 'a+')
    total = ans.tell()
    num = total / ONE_SUDOKU
    r1 = random.randint(0, num)
    ans.seek(r1*ONE_SUDOKU, 0)
    for i in range(9):
        transformed.append(ans.readline().rstrip().split(' '))
    transformer(transformed)
    output = open("sud", 'a')
    for a in range(9):
        for b in range(9):
            if b == 8:
                output.write(str(transformed[a][b])+'\n')
            else:
                output.write(str(transformed[a][b])+' ')
    output.write('\n')
    print("-----Done Transforming----\n")
    time.sleep(2)
