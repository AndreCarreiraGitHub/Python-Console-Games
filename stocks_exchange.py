import pandas as pd
from tabulate import tabulate
from config import RED, GREEN, YELLOW, MAGENTA,BLUE, RESET
import random

# Load data
stock_data = pd.read_csv("stock_exchange/stock.csv")
balance_data = pd.read_csv("stock_exchange/balance.csv")
balance = float(balance_data.iat[0,0])
turn = int(balance_data.iat[1,0])
my_stocks = None

def get_valid_input(prompt, valid_options):
    while True:
        response = input(prompt)
        if response.isdigit() and int(response) in valid_options:
            return int(response)
        print("Invalid input, please try again.")


def display_menu():
    show_stocks()
    print("\nWhat would you like to do today?")
    print("1: View Balance")
    print("2: View Stock Market")
    print("3: Advance a Day")
    print("4: Quit")
    return get_valid_input("Choose an option: ", {1, 2, 3, 4})


def check_balance():
    print(f"\nCurrent Balance: {BLUE}£{balance}{RESET}")
    print(f"Your stocks: {BLUE}£{my_stocks}{RESET}")


def show_stocks():
    formatted_stocks = []
    for y in range(stock_data.shape[0]):
        name, code, price = stock_data.iloc[y, [0, 1, 4]]
        color = GREEN if stock_data.iloc[y, 4] > stock_data.iloc[y, 3] else RED
        formatted_stocks.append([f"{color}{name}{RESET}", f"{MAGENTA}{code}{RESET}", f"{YELLOW}£{price}{RESET}"])
    print(tabulate(formatted_stocks, headers=["Name", "Code", "Price"], tablefmt="grid"))


def purchase_stocks():
    global balance  # Declare 'balance' as global at the beginning of the function
    code = input("Enter the stock code you want to purchase: ")
    shares = get_valid_input("How many shares would you like to buy? ", range(1, 100000))
    found_match = False
    for index, row in stock_data.iterrows():
        if code == row['Code']:  # Assuming 'Symbol' is the column name for stock codes
            found_match = True
            total_cost = row['Current Price'] * shares  # Assuming 'Price' is the column name for stock prices
            if balance >= total_cost:
                balance -= total_cost
                print(f"\n{GREEN}Purchase successful.{RESET} Remaining balance: £{balance}")
                break  # Exit the loop as soon as a match is found and processed
            else:
                print(f"\n{RED}Insufficient balance.{RESET}")
                break  # Exit the loop because there is no need to check further if the user can't afford this stock

    if not found_match:
        print("No match found.")


def inflation_simulator():
    random_change = random.gauss(drift, volatility)  # Gaussian distribution
    new_price = previous_price * (1 + random_change)
    return max(new_price, 0), positive
    positive = random.choice([True, False])
    
def advance_day():
    global turn, stock_data
    turn += 1
    print("Day: ", turn)
    for index, row in stock_data.iterrows():
        inflation, positive = inflation_simulator()
        previous_price = row['Current Price']
        if positive:
            new_price = round(previous_price * (1 + inflation), 2)  # Calculate the new price after inflation
        else:
            new_price = round(previous_price * (1 - inflation), 2)  # Calculate the new price after deflation
        
        # Update the DataFrame
        stock_data.at[index, 'Previous Price'] = previous_price
        stock_data.at[index, 'Current Price'] = new_price
        

def main():
    while True:
        choice = display_menu()
        if choice == 1:
            check_balance()
        elif choice == 2:
            purchase_stocks()
        elif choice == 3:
            advance_day()
        elif choice == 4:
            print("Goodbye!")
            break

if __name__ == "__main__":
    print("Welcome to the Stock Exchange Game!")
    print("Day: ",turn)
    main()