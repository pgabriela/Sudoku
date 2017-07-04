from django.shortcuts import render
from .models import Quiz
from random import randint
import copy
from django.http import HttpResponse
from django import forms
from .forms import InputAns

EASY_BLANK = 30
MODERATE_BLANK = 45
HARD_BLANK = 65


def theGame(request, level):
    num = Quiz.objects.count()
    r1 = randint(0, num-1)
    solution = Quiz.objects.all()[r1]

    solutionMatrix = []
    solArr = solution.solution.rstrip().split(',')
    for i in range(9):
        solutionMatrix.append([])
    for i in range(9):
        for j in range(9):
            solutionMatrix[i].append(solArr[i*9+j])

    solutionMatrix2 = copy.deepcopy(solutionMatrix)
    if(int(level) == 0):
        quizMatrix = easy(solutionMatrix)
    elif(int(level) == 1):
        quizMatrix = moderate(solutionMatrix)
    else:
        quizMatrix = hard(solutionMatrix)

    form = InputAns()
    for i in range(9):
        for j in range(9):
            if quizMatrix[i][j] == '0':
                form.__dict__['fields']['c%s_%s' % (str(i), str(j))] =\
                    forms.CharField(max_length=1, min_length=1, strip=True,
                                    widget=forms.TextInput(attrs={
                                        'size': 1,
                                    }))

    return render(request, 'SudokuGame/home.html',
                  {
                      'quizMatrix': quizMatrix,
                      'solPk': solution.pk,
                      'solutionMatrix': solutionMatrix2,
                      'form': form,
                  })


def hard(solutionMatrix):
    solutionMatrix2 = copy.deepcopy(solutionMatrix)
    counter = 0
    while(counter < HARD_BLANK):
        rR = randint(0, 8)
        rC = randint(0, 8)
        if(solutionMatrix2[rR][rC] == '0'):
            continue
        else:
            solutionMatrix2[rR][rC] = '0'
            counter += 1
    return solutionMatrix2


def easy(solutionMatrix):
    solutionMatrix2 = copy.deepcopy(solutionMatrix)
    counter = 0
    while(counter < EASY_BLANK):
        rR = randint(0, 8)
        rC = randint(0, 8)
        if(solutionMatrix2[rR][rC] == '0'):
            continue
        else:
            solutionMatrix2[rR][rC] = '0'
            counter += 1
    return solutionMatrix2


def moderate(solutionMatrix):
    solutionMatrix2 = copy.deepcopy(solutionMatrix)
    counter = 0
    while(counter < MODERATE_BLANK):
        rR = randint(0, 8)
        rC = randint(0, 8)
        if(solutionMatrix2[rR][rC] == '0'):
            continue
        else:
            solutionMatrix2[rR][rC] = '0'
            counter += 1
    return solutionMatrix2


def checkAns(request, solPk):
    ansModel = Quiz.objects.get(pk=solPk)
    ansModel = ansModel.solution.rstrip().split(',')
    for i in request.POST.items():
        if(len(i[0]) != 4):
            continue
        row = i[0][1]
        col = i[0][3]
        if(ansModel[int(row)*9+int(col)] == i[1]):
            continue
        else:
            return HttpResponse("False")
    return HttpResponse("True")


def chooser(request):
    return render(request, 'SudokuGame/choose.html', {})
