
import random 
correct_number=random.randint(0,100)
guess=0
guesses=0
while guess!=correct_number and guesses<10:
    guess=int(input(' guess a number from 0 to 100: '))
    guesses=guesses+1

    if guess==correct_number:
        print ('Congratulations! You won.')
    elif guess>correct_number:
        print ('your guess is too high')
        print ('Guesses remaining:',10-guesses)
    elif guess<correct_number:
            print ('your guess is too low')
            print ('Guesses remaining:',10-guesses)
    else:
        print ('Sorry! You lost.the number was: ',correct_number)
        
