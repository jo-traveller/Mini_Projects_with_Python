print("Welcome to my comupter")

playing = input("Do you want to play? hello")

print(playing)

if playing.lower() != "yes":
    quit()


print("Okay! Let's play :) ")


score = 0

answer = input("What does CPU Stand for ?  ")
if answer.lower() == "central processing unit":
   print('correct!')
   score += 1
else:
    print("Incorrect!")

    answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    score += 1
    print('Correct!')

    
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1

   
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1


print ("you got " + str(score)+"questions correct")
