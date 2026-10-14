import random
def game():
    print("you are playing the game")
    score = random.randint(1,100)
    with open("hiscore.txt") as f:
        hiscore = f.read()
    if hiscore != "":
        hiscore = int(hiscore)
    else:
        hiscore = 0
    print(f"you score: {score}")
    if(score>hiscore):
        with open("hiscore.txt","w") as f:
            f.write(str(score))
game()