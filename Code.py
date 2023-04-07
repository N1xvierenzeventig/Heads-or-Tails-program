import random
# You're a playing a game for money. You flip the coin. If it is side which you said it would be you're imporving your balance twice as many as it was then you're diciding do you have to play this game further and win more money or you do want to quit with your just earned new money.
# Heads = 0
# Tails = 1
Game = True
Won = True

def game(Game, Won):
    Global_Balance = 0
    Balance = int(input("With what amount of money do you want to play in game: "))
    Starting_Balance = Balance
    while Game == True:
            if Won is False:
                Balance = int(input("With what amount of money do you want to play in game: "))
            else:
                Balance = Balance
            Your_move = input("What do you choose Heads or Tails: ")
            b = random.randint(0, 1)
            if Your_move == "Heads" and b == 0:
                Balance *= 2
                print("You won this round it was Heads.Your current balance is " + str(Balance) + "€.")
                Won = True
                Your_Choice = input("Do you want to continue the game ")
                if Your_Choice == "No":
                    Global_Balance = Global_Balance + Balance
                    return("You won " + str(Global_Balance)+ "€.")
                elif Your_Choice == "Yes":
                    Game = True

            elif Your_move == "Tails" and b == 1:
                Balance *= 2
                print("You won this round it was Tails.Your current balance is " + str(Balance) + "€.")
                Won = True
                Your_Choice = input("Do you want to continue the game ")
                if Your_Choice == "No":
                    Global_Balance = Global_Balance + Starting_Balance
                    return ("You won " + str(Global_Balance) + "€.")
                elif Your_Choice == "Yes":
                    Game = True
            elif Your_move == "Heads" or "heads" and b == 1:
                Your_Choice = input("You have lost your " + str(Balance) + "€. Do you want to play this game once more?:")
                Global_Balance = Global_Balance - Starting_Balance
                Won = False
                if Your_Choice == "No":
                    return ("You lost " + str(Global_Balance) + "€.")
                elif Your_Choice == "Yes":
                    Game = True
            elif Your_move == "Tails" or "tails" and b == 0:
                Your_Choice = input("You have lost your " + str(Balance) + "€. Do you want to play this game once more?:")
                Global_Balance = Global_Balance - Starting_Balance
                Won = False
                if Your_Choice == "No":
                    return ("You lost " + str(Global_Balance) + "€.")
                elif Your_Choice == "Yes":
                    Game = True
print(game(Game, Won))