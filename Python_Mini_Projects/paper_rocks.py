import random

# intialize user and computer score
user_wins = 0 
computer_wins = 0

# make a list (i dont remember exactly if it is tuple or list but i will check later)
options = ["rock","paper","scissors"]

#make a loop to allow
while True:
  user_input = input("type Rock/paper/scissors or Q to quit").lower()
  if user_input == "q":
   break
   
   if user_input not in options:

    continue

  random_number =random.randint(0,2) 
  # rock: 0 , paper: 1 , scissors: 2
  computer_pick = options[random_number]
  print("computer picked", computer_pick + "." )
  if user_input == "rock" and computer_pick =="scissors":
    print("You won")
    user_wins += 1
    continue
  
  elif user_input == "paper" and computer_pick =="rock":
    print("You won")
    user_wins += 1
    continue
  
  elif user_input == "scissors" and computer_pick =="paper":
    print("You won")
    user_wins += 1
    continue
  elif user_input == computer_pick:
        print("Tie!")
        
  else:print("you lost!")
  computer_wins += 1
  
    

print("you won ",user_wins," times")

print("the computer won ",computer_wins," times")

print("Goodbye!") 