import random

def game():
    print("you are playing game ")
    score=random.randint(1,100)
    with open("/Users/amankesarwani/Desktop/Python/File I:O/game.txt") as f:
        HighScore=f.read()
        if HighScore !="":
            HighScore= int(HighScore)
        else:
            HighScore=0

    print(f"Score is:{score}")


    if score>HighScore:
        with open("/Users/amankesarwani/Desktop/Python/File I:O/game.txt","w") as f:
            f.write(str(score))
    return score

game()

