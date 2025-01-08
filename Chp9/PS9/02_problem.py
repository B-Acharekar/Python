# 2. The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘hiscore.txt’ which is either blank or
# contains the previous hiscore. 
# You need to write a program to update the Hiscore whenever the game() function breaks the hiscore.

import random 
def game():
    print("Your are playing a game...")
    score = random.randint(0,99)
    #Fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"Your score:{score}")
    if (score>hiscore or hiscore ==""):
        # write this hiscore to the file
        with open("hiscore.txt",'w') as f:
            f.write(str(score))
    return score

game()
