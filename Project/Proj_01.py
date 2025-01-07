#  SNAKE, WATER, GUN GAME
# Following are the rules of the game:

# Snake vs. Water: Snake drinks the water hence wins.
# Water vs. Gun: The gun will drown in water, hence a point for water
# Gun vs. Snake: Gun will kill the snake and win.

'''
1 for snake
0 for water
-1 for gun
'''
import random
print('Snake - Water - Gun')


options ={"s":1, "w":0, "g":-1}
revOptions = {1:"Snake", 0:"Water", -1:"Gun"}

computerChoice = random.choice(list(options.values()))

userInput = input('Enter your choice (s,w,g): ')
if userInput not in options:
    print("Invalid input! Please choose 's', 'w', or 'g'.")
    exit()

userChoice = options[userInput]


print(f"You chose {revOptions[userChoice]} \nComputer choose {revOptions[computerChoice]}")
if computerChoice == userChoice:
    print("It is a tie!")
else:
    if (computerChoice == -1 and userChoice == 1):
        print('You lose!')
    elif (computerChoice == -1 and userChoice == 0):
        print('You win!')
    elif (computerChoice == 1 and userChoice == 0):
        print('You lose!')
    elif(computerChoice == 1 and userChoice == -1):
        print('You win!')
    elif(computerChoice == 0 and userChoice == 1):
        print('You lose!')
    elif(computerChoice == 0 and userChoice == -1):
        print('You win!')
    else:
        print('something went wrong!')



