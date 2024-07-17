import subprocess
import os
import platform
from rockpaperscissors import winRPS, loseRPS
from blackjack import winB, loseB

win = winB + winRPS
lose = loseB + loseRPS

# Function to clear the terminal
def clear_terminal():
    # Check the operating system
    current_os = platform.system()
    
    if current_os == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Call the function to clear the terminal
clear_terminal()

print("Which game would you like to play?\n")

print("Current record W/L: ", win, "/", lose, "\n")

print("Rock Paper Scissors: 1")
print("Blackjack: 2\n")

answer = int(input("You: "))

if answer == 1:
    subprocess.run(["python", "rockpaperscissors.py"])
elif answer == 2:
    subprocess.run(["python", "blackjack.py"])