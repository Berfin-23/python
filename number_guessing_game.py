import random

print("\nWelcome to my number guessing game")
print("\nRules:\n1)Enter a number greater than 0\n2)Try to guess the number\n3)The system will give some hints\n4)Take less than 5 guesses to win the game")

inp = input("Enter a number: ")

if inp.isdigit():
    inp = int(inp)

    if inp <= 0 :
        print("Enter a number greater than zero next time:)")
        quit()

else:
    print("Enter a number next time:)")
    quit()

ran_num = random.randint(0,inp)
nguess = 0

while True:
    nguess += 1
    guess = input("Enter your guess : ")
    if guess.isdigit():
        guess = int(guess)

    else:
        print("Enter a number next time")
        continue

    if guess == ran_num:
        print("You got it!")
        break

    elif guess > ran_num :
        print("You are above the number!")

    else :
        print("You are below the number!")

print("You got it in ",nguess," guesses")
if nguess >=5:
    print("You lost:(")

else:
    print("You won:)")
