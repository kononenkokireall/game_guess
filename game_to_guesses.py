# this is Game guessesTaken

import random as rd

guessesTaken = 0

print('Hello my Friend!')
print('What is your name?')
myName = input()
print(f'Nice to meat you {myName}')

number = rd.randint(1, 10)

for guessesTaken in range(6):
    print(f'Let`s play my Game {myName}')
    guess = input()
    guess = int(guess)

    if guess > number:
        print(f'Too big {myName} try again')
        
    if guess < number:    
        print(f'Too smoll {myName} try again')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print(f'Perfectly {myName}, you Win {guessesTaken}')

if guess != number:
    number = str(number)
    print(f'So far, you lose {myName}, my number {number}')
