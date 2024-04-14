from colorama import just_fix_windows_console, Fore, Back, Style
from time import sleep

just_fix_windows_console()

#  A Line
countOfLines = 10

#  AnimationSymbols
firstSymbol = ' '
lastSymbol = '='

#  AnimationSpeed
animationInterval = 1  #  interval in seconds
speedCoef = 0.9
speedCap = 0

#  AnimationMultiplier
coef = 1
coefStep = 1
coefMin = 0
coefStartMax = 5  #  start max
coefMax = coefStartMax
maxExpand = 1
coefRealMax = 1500

#  Functionality
for i in range(1,countOfLines):
    while(True):
        sleep(animationInterval)
        coef += coefStep
        print(Back.RED, firstSymbol*coef,Back.GREEN, lastSymbol, end='\r')
        print()
        if coef == coefMax:
            animationInterval *= speedCoef * (i*0.5)
            coefStep = -coefStep
        elif coef == coefMin:
            coefMax += maxExpand
            coefStep = -coefStep
        if coefMax == coefRealMax:
            maxExpand += -maxExpand
        elif coefMax == coefMin:
            maxExpand += -maxExpand
            
