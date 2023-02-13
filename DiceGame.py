# Cianee Sumowalt
# This program simulates the dice game 'craps'
# 6 October, 2022


import random
print ("This game simulates the dice game 'craps.'")
print ("")

def rolldice():
    # Alows user to roll dice between 1 to 6.
    value = random.randint(1,6)
    return value

die1 = rolldice()
die2 = rolldice()
sumDie = die1 + die2 #This is for the initial die roll that determines if you win or lsoe.
print(f"You rolled {die1} and {die2}.")
print (f"The sum of the dice is {sumDie}.")

if sumDie in (7,11):
    gameStatus = "win"
elif sumDie in (2,3,12):
    gameStatus = "loser"
else:
    currentDie = sumDie
    gameStatus = "continue"
    print (f"Continue, the point is {currentDie}.")


def thePoint(gameStatus):
    while gameStatus == "continue":
        dice3 = rolldice()
        dice4 = rolldice()
        print (f"You rolled {dice3} and {dice4}.")
        compDie = dice3 + dice4
        if compDie == currentDie:
            return print ("Player wins.")
        if compDie == 7:
            return print ("Player loses.")



thePoint(gameStatus)

if gameStatus == "win":
    print("Player wins.")
if gameStatus == "loser":
    print("Player loses.")



