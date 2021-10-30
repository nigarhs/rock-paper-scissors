from random import randint

t=["Rock","Paper","Scissors"]

computer=t[randint(0,2)]
player=False

while player==False:
    player=input("Rock,Paper,Scissors ?\n")
    if player==computer:
        print("TIE!")

    elif player=="Rock":
        if computer=="Paper":
            print("You lose!\n" ,computer, "covers" ,player)
        else:
            print("You win! \n",player,"smashes",computer)

    elif player=="Paper":
        if computer=="Scissors":
            print("You lose!\n", computer ,"cut", player)
        else:
            print("You win!\n", computer ,"covers",player)

    elif player=="Scissors":
        if computer=="Rock":
            print("You lose!\n",computer,"smashes",player)
        else:
            print("You win!\n",player,"cut",computer)


    else:
        print("CHECK YOUR SPELLING")
    player=False
    computer=t[randint(0,2)]



