#monty hall problem
#3 doors
#1 door has a big prize! (car)
#Other 2 have a goat
#The contestant gets to pick one of the doors

#(car) (G) (G)
#      (Y)

#Write a function that takes 1 parameter, the number of games to play
#loop that many times (game many times)
#generate two random numbers
#   position of the car
#   Choice of the player
#Remove one of the non-chosen goats from the game
#Determine if the player switches will they win more?
#if they win from switching, add 1 to a win counter
#otherwise, add 1 to a loss counter
#print out perecentage of lossess and wins
##########################################
#function block
import random
def monty_hall(games):
    loss = 0
    wins = 0
    for i in range(games):
        car =random.randrange(0,3)
        choice= random.randrange(0,3)
        
        
        if choice == car:
            loss += loss
            
        if choice != car:
            wins += wins
        loss_percentage=loss/games * 100
        win_percentage=wins/games * 100
    return print([win_percentage,loss_percentage])
##################################
# main block
x=int(input("How many games would you like to play?"))
print("Win percentage vs loss percentage")
monty_hall(x)