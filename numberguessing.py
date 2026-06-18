import random
number=random.randint(1,100)
guess=0
attempt=0
while(guess!=number):
      guess=int(input("Guess a number:"))
      attempt = attempt+1
      if(guess<number):
          print("Guess higher")
      elif(guess>number):
          print("Guess Lower")
      else:
           print("You won in ",attempt," attempts")

    
