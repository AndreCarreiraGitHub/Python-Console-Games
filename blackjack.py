import subprocess
import random
from config import win, lose, RED, GREEN, YELLOW, BLUE, MAGENTA, RESET, line, change_line

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
cardsName = ["1","2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]

def draw_card():
    playerCard = random.randint(0, 13)
    aiCard = random.randint(0, 13)
    return playerCard, aiCard

print("")
print("Welcome to Blackjack!")
print("Are you ready to start?")

answer = input("You: ")

if answer != "Yes" and answer != "yes":
    while answer != "Yes" and answer != "yes":
        print("Are you sure you're not ready to start?")
        answer = input("You: ")

continue_playing = True
playerScore = 0
aiScore = 0

while continue_playing == True:
    playerCard, aiCard = draw_card()
    
    playerScore = playerScore + cards[playerCard]
    aiScore = aiScore + cards[aiCard]
    
    if playerScore < 21 and aiScore < 21:
        print("")
        print("Player: ", cardsName[playerCard], " for a total score of: ", playerScore)
        print("AI: ", cardsName[aiCard], " for a total score of: ", aiScore)
        print("")
        print("Would you like to continue playing?")
        answer = input("You: ")
        
        if answer != "Yes" and answer != "yes":
            continue_playing = False
    else:
        print("")
        if playerScore == 21 and aiScore != 21:
            print("You've got 21! You win!")
            win+=1
            change_line("info.txt", 1, str(win))
        elif aiScore == 21 and playerScore != 21:
            print("AI's got 21, you lose...")
            lose+=1
            change_line("info.txt", 2, str(lose))
        elif playerScore > 21 and aiScore < 22:
            print("You've gone bust, you lose...")
            lose+=1
            change_line("info.txt", 2, str(lose))
        elif aiScore > 21 and playerScore < 22:
            print("AI went bust! You win!")
            win+=1
            change_line("info.txt", 1, str(win))
        continue_playing = False

print("")
print(line)
print("")

subprocess.run(["python", "mainmenu.py"])