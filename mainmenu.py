import subprocess
import os
import platform
from config import win, lose, RED, GREEN, YELLOW, BLUE, MAGENTA, RESET, turn, change_line

# Function to clear the terminal
def clear_terminal():
    # Check the operating system
    current_os = platform.system()
    
    if current_os == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Call the function to clear the terminal
if turn == 0:
    clear_terminal()

turn = change_line("info.txt", 3, "1")

print("Which game would you like to play?\n")

print("Current record W/L: ", win, "/", lose, "\n")

print("Rock Paper Scissors: 1")
print("Blackjack: 2")
print("Stocks Exchange: 3\n")

answer = int(input("You: "))

while answer != 1 and answer != 2 and answer != 3:
    print("Please provide a valid answer.")
    answer = int(input("You: "))

if answer == 1:
    subprocess.run(["python", "rockpaperscissors.py"])
elif answer == 2:
    subprocess.run(["python", "blackjack.py"])
elif answer == 3:
    subprocess.run(["python", "stocks_exchange.py"])