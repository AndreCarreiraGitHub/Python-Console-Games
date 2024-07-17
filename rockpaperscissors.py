import random
import subprocess
import shutil

#Setting up where each value will be stored into
rock = 1
paper = 2
scissor = 3

#Get console width
columns, _ = shutil.get_terminal_size()

#Create a line that spans the width of the screen
line = '_' * columns

winRPS=0
loseRPS=0

#Setting up colours
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
RESET = "\033[0m"

#Console writting with game rules (the values descriptions will be displayed on the console with the colour as per the code)
print("Welcome to Rock, Paper and Scissors!")
print("The options are as follow: \n")
print(f"{BLUE}Rock: 1{RESET}")
print(f"{MAGENTA}Paper: 2{RESET}")
print(f"{YELLOW}Scissor: 3{RESET} \n")

def pick_the_winner(userChoice, aiChoise):
    if userChoice == 1:
        if aiChoise ==2:
            winner = 2
        elif aiChoise == 3:
            winner = 1
        elif aiChoise == 1:
            winner = 3
    elif userChoice == 2:
        if aiChoise ==2:
            winner = 3
        elif aiChoise == 3:
            winner = 1
        elif aiChoise == 1:
            winner = 2
    elif userChoice == 3:
        if aiChoise ==2:
            winner = 1
        elif aiChoise == 3:
            winner = 3
        elif aiChoise == 1:
            winner = 2
    return winner    

def ai_choice_print(aiChoice):
    if aiChoice == 1:
        print("Ai has picked: ", f"{BLUE}Rock{RESET}")
    elif aiChoice == 2:
        print("Ai has picked: ", f"{MAGENTA}Paper{RESET}")
    elif aiChoice == 3:
        print("Ai has picked: ", f"{YELLOW}Scissor{RESET}")

def rock_paper_scissor_ai(userChoice):
    aiChoise = random.randint(1, 3)
    winner = pick_the_winner(userChoice, aiChoise)
    ai_choice_print(aiChoise)
    return winner

#Asking for user input
answerInt = int(input("You: "))

#While answer out of range ask again
while answerInt > 3:
    print("Answer chosen not within range, please try again.")
    answerInt = int(input("You: "))

resetColor = {RESET}

if answerInt == 1:
    answer = "Rock"
    color = f"{BLUE}"
elif answerInt == 2:
    answer = "Paper"
    color = f"{MAGENTA}"
elif answerInt == 3:
    answer = "Scissors"
    color = f"{YELLOW}"
    
print("")
print("You have chosen: ", color, answer, resetColor)
print("")

result = rock_paper_scissor_ai(answerInt)

if result == 1:
    print(f"{GREEN}You win!{RESET}")
    winRPS+=1
elif result == 2:
    print(f"{RED}You lost...{RESET}")
    loseRPS+=1
elif result == 3:
    print(f"{YELLOW}A draw...{RESET}")
    
print("")
print(line)
print("")

subprocess.run(["python", "main.py"])