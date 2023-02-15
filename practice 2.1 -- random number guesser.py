import random

num = random.randint(1,100)
tries =0

while tries <3:
    guess = int(input(f"I've chosen a number between 1 and 100. You have {3-tries} guesses. Please guess a number: "))
    if guess == num:
        print("you got it right! Congrats!")
        break
    elif guess < num:
        print ("Go a little higher.")
        tries+=1
        print (f"You have {3-tries} tries left.")
        continue
    elif guess > num:
        print("Go a little lower.")
        tries += 1
        print(f"You have {3 - tries} tries left.")
        continue
else:
    print("gameover!")
