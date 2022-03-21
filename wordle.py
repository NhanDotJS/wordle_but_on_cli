#!/usr/bin/env python3
# pycodestyle: disable=line-too-long
from multiprocessing.connection import answer_challenge
import sys
from termcolor import colored, cprint
import random


print('''

 _    _  _____ ______ ______  _      _____             
| |  | ||  _  || ___ \|  _  \| |    |  ___|            
| |  | || | | || |_/ /| | | || |    | |__              
| |/\| || | | ||    / | | | || |    |  __|             
\  /\  /\ \_/ /| |\ \ | |/ / | |____| |___             
 \/  \/  \___/ \_| \_||___/  \_____/\____/             
                                                       
                                                       

                                                       
 _             _                    _____  _     _____ 
| |           | |                  /  __ \| |   |_   _|
| |__   _   _ | |_    ___   _ __   | /  \/| |     | |  
| '_ \ | | | || __|  / _ \ | '_ \  | |    | |     | |  
| |_) || |_| || |_  | (_) || | | | | \__/\| |_____| |_ 
|_.__/  \__,_| \__|  \___/ |_| |_|  \____/\_____/\___/ 


''')  # noqa # Credit to: patorjk https://patorjk.com/software/taag


win = False

# Credit:dracos https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93
validWordListFile = './valid-wordle-words.txt'
with open(validWordListFile, 'r') as f:
    validWordList = f.read().split('\n')

# answer = 'dated'
answer = random.choice(validWordList)

displayChars = [
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ']]


def printOutput():
    print(f'''
    +---+---+---+---+---+
    | {displayChars[0][0]} | {displayChars[0][1]} | {displayChars[0][2]} | {displayChars[0][3]} | {displayChars[0][4]} |
    +---+---+---+---+---+
    | {displayChars[1][0]} | {displayChars[1][1]} | {displayChars[1][2]} | {displayChars[1][3]} | {displayChars[1][4]} |
    +---+---+---+---+---+
    | {displayChars[2][0]} | {displayChars[2][1]} | {displayChars[2][2]} | {displayChars[2][3]} | {displayChars[2][4]} |
    +---+---+---+---+---+
    | {displayChars[3][0]} | {displayChars[3][1]} | {displayChars[3][2]} | {displayChars[3][3]} | {displayChars[3][4]} |
    +---+---+---+---+---+
    | {displayChars[4][0]} | {displayChars[4][1]} | {displayChars[4][2]} | {displayChars[4][3]} | {displayChars[4][4]} |
    +---+---+---+---+---+
    | {displayChars[5][0]} | {displayChars[5][1]} | {displayChars[5][2]} | {displayChars[5][3]} | {displayChars[5][4]} |
    +---+---+---+---+---+
    ''')  # noqa


# printOutput()
def takeInput():
    while True:
        guess = input('Please type in your guess: ').lower()
        if len(guess) != 5:
            print('Your guess must be 5 characters')
        elif guess not in validWordList:
            print('Your guess is not in wordlist')
        else:
            return verifyWord(guess, answer)


def verifyWord(guess, answer):
    result = []
    colorList = []
    if guess == answer:
        colorList = ['green', 'green', 'green', 'green', 'green']
        for char in guess:
            formatted = colored(char, 'green')
            result.append(formatted)
        return result, True
    else:
        charToFind = list(answer)
        colorList = []
        for x in range(len(guess)):
            color = 'white'
            if guess[x] in charToFind:
                if charToFind[x] == guess[x]:
                    color = 'green'
                else:
                    color = 'yellow'
                charToFind[charToFind.index(guess[x])] = ''
            colorList.append(color)
        for x in range(len(guess)):
            formatted = colored(guess[x], colorList[x])
            result.append(formatted)
        return result, False


for x in range(6):
    printOutput()
    displayChars[x], win = takeInput()
    if win:
        break

if win:
    printOutput()
    print('''
__   _______ _   _   _    _  _____ _   _ 
\ \ / /  _  | | | | | |  | ||  _  | \ | |
 \ V /| | | | | | | | |  | || | | |  \| |
  \ / | | | | | | | | |/\| || | | | . ` |
  | | \ \_/ / |_| | \  /\  /\ \_/ / |\  |
  \_/  \___/ \___/   \/  \/  \___/\_| \_/
                                         
                                         ''')  # noqa
else:
    printOutput()
    print('''
__   _______ _   _   _     _____ _____ _____ 
\ \ / /  _  | | | | | |   |  _  /  ___|_   _|
 \ V /| | | | | | | | |   | | | \ `--.  | |  
  \ / | | | | | | | | |   | | | |`--. \ | |  
  | | \ \_/ / |_| | | |___\ \_/ /\__/ / | |  
  \_/  \___/ \___/  \_____/\___/\____/  \_/  
                                             
                                         ''')  # noqa
    print(f'The word is: {answer}')
# displayChars[0] = takeInput()
# printOutput()
