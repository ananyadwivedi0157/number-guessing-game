import random 
guess=0
guesses=0
level=int(input("1.easy\n2.medium\n3.hard\nchoose a level:"))
if level==1:
     correct_number=random.randint(0,50)
     while guess!=correct_number and guesses<10:
      guess=int(input(' guess a number from 0 to 50: '))
      guesses=guesses+1

      if guess==correct_number:
        print ('Congratulations! You won.')
      elif guess>correct_number:
        print ('your guess is too high')
        print ('Guesses remaining:',10-guesses)
      elif guess<correct_number:
            print ('your guess is too low')
            print ('Guesses remaining:',10-guesses)
     if guess!=correct_number:
        print ('Sorry! You lost.the number was: ',correct_number)
elif level==2:
    correct_number=random.randint(0,100)
    while guess!=correct_number and guesses<7:
          guess=int(input(' guess a number from 0 to 100: '))
          guesses=guesses+1
    
          if guess==correct_number:
            print ('Congratulations! You won.')
          elif guess>correct_number:
            print ('your guess is too high')
            print ('Guesses remaining:',7-guesses)
          elif guess<correct_number:
                print ('your guess is too low')
                print ('Guesses remaining:',7-guesses)
    if guess!=correct_number:
            print ('Sorry! You lost.the number was: ',correct_number)
elif level==3:
      correct_number=random.randint(0,500)
      while guess!=correct_number and guesses<5:
                guess=int(input(' guess a number from 0 to 500: '))
                guesses=guesses+1
          
                if guess==correct_number:
                  print ('Congratulations! You won.')
                elif guess>correct_number:
                  print ('your guess is too high')
                  print ('Guesses remaining:',5-guesses)
                elif guess<correct_number:
                      print ('your guess is too low')
                      print ('Guesses remaining:',5-guesses)
      if guess!=correct_number:
                  print ('Sorry! You lost.the number was: ',correct_number)

