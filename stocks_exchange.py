import pandas as pd
from tabulate import tabulate
from config import RED, GREEN, YELLOW, MAGENTA,BLUE, RESET
import random
import numpy as np

# Load data
stock_data = pd.read_csv("stock_exchange/stock.csv")
balance_data = pd.read_csv("stock_exchange/balance.csv")
balance = float(balance_data.iat[0,0])
turn = int(balance_data.iat[1,0])
my_stocks_value = []
my_stocks_shares = {
    'TJM': 0,
    'WMT': 0,
    'AND': 0,
    'WYK': 0
}
my_stocks_trend = [[] for _ in range(stock_data.shape[0])]
stock_trend = [[] for _ in range(stock_data.shape[0])]

def get_valid_input(prompt, valid_options):
    while True:
        response = input(prompt)
        if response.isdigit() and int(response) in valid_options:
            return int(response)
        print("Invalid input, please try again.")


def display_menu():
    print("\nWhat would you like to do today?")
    print("1: View Balance")
    print("2: View Stock Market")
    print("3: Advance a Day")
    print("4: Sell Stock")
    print("5: Quit")
    return get_valid_input("Choose an option: ", {1, 2, 3, 4, 5})


def check_balance():
    print(f"\nCurrent Balance: {BLUE}£{balance}{RESET}")
    print(f"Your stocks: {BLUE}£{my_stocks_value}{RESET}")


def show_stocks():
    formatted_stocks = []
    for y in range(stock_data.shape[0]):
        name, code, price = stock_data.iloc[y, [0, 1, 4]]
        trend = stock_trend[y]
        if len(trend) > 1:  # Ensure there are at least two prices to compare
            trend_symbols = ''.join(['+' if trend[i] < trend[i+1] else '-' if trend[i] > trend[i+1] else '=' for i in range(len(trend)-1)])
        else:
            trend_symbols = 'N/A'  # Not enough data to determine trend

        color = GREEN if stock_data.iloc[y, 4] > stock_data.iloc[y, 3] else RED
        
        formatted_stocks.append([f"{color}{name}{RESET}", f"{MAGENTA}{code}{RESET}", f"{YELLOW}£{price}{RESET}", f"{BLUE}{trend_symbols}{RESET}"])
    formatted_stocks.append([f"{color}Your Stocks{RESET}", f"{MAGENTA}YOU{RESET}", f"{YELLOW}£{sum(my_stocks_value)}{RESET}", f"{BLUE}{trend_symbols}{RESET}"])
    print(tabulate(formatted_stocks, headers=["Name", "Code", "Price", "Trend"], tablefmt="grid"))


def purchase_stocks():
    global balance,stock_trend,my_stocks_shares,my_stocks_trend,my_stocks_value
    code = input("Enter the stock code you want to purchase: ")
    shares = get_valid_input("How many shares would you like to buy? ", range(1, 100000))
    found_match = False
    for index,row in stock_data.iterrows():
        if code == row['Code']:  # Assuming 'Symbol' is the column name for stock codes
            found_match = True
            total_cost = row['Current Price'] * shares  # Assuming 'Price' is the column name for stock prices
            if balance >= total_cost:
                balance -= round(total_cost,2)
                print(f"\n{GREEN}Purchase successful.{RESET} Remaining balance: £{balance}")
                my_stocks_shares[code] += shares
                print(my_stocks_shares)
                calculate_personal_stock_value()
                break  # Exit the loop as soon as a match is found and processed
            else:
                print(f"\n{RED}Insufficient balance.{RESET}")
                calculate_personal_stock_value()
                break  # Exit the loop because there is no need to check further if the user can't afford this stock

    if not found_match:
        print("No match found.")


def calculate_personal_stock_value():
    global my_stocks_value  # Ensure my_stocks_value is updated globally
    my_stocks_value = []  # Reset my_stocks_value to recalculate
    for stock_code, shares in my_stocks_shares.items():
        # Find the corresponding row in stock_data
        stock_row = stock_data[stock_data['Code'] == stock_code]
        if not stock_row.empty:
            current_price = stock_row.iloc[0]['Current Price']  # Assuming 'Current Price' is the column name
            stock_value = round(shares * current_price,2)
            my_stocks_value.append(stock_value)
    show_stocks()
    
    
def calculate_specific_stock_value(code,shares):
    correct_row = stock_data[stock_data['Code'] == code]
    current_price = correct_row['Current Price'].values[0]
    print("Current Price: ", current_price)
    
    sale_value = current_price * shares
    
    return sale_value
    
    
def inflation_simulator(previous_price,volatility=0.07):
    dt = 1  # One time step; e.g., one day
    drift = np.random.uniform(-0.0005, 0.0005)
    random_shock = np.random.normal(drift * dt, volatility * np.sqrt(dt))
    new_price = previous_price * np.exp(random_shock)  # Continuous compounding
    return max(new_price, 0.01)  # Avoid non-positive prices
    

def update_trend_for_stock(index, new_price):
    stock_trend[index].append(new_price)
    if len(stock_trend[index]) > 8:
        stock_trend[index].pop(0)


def advance_day():
    global turn, stock_data
    turn += 1
    print("Day: ", turn)
    x=0
    for index, row in stock_data.iterrows():
        previous_price = round(row['Current Price'],2)
        new_price = round(inflation_simulator(previous_price),2)  # Calculate the new price after inflation
        update_trend_for_stock(x,new_price)
        
        # Update the DataFrame
        stock_data.at[index, 'Previous Price'] = previous_price
        stock_data.at[index, 'Current Price'] = new_price
        x+=1
    calculate_personal_stock_value()
        
        
def sell_stock():
    global balance
    print("\n",my_stocks_shares)
    print("Any particular stock you'd like to sell?")
    print("1: Yes")
    print("2: No")
    answer = get_valid_input("Choose an option: ", {1, 2})
    if answer == 1:
        print("Please write the code of which stock you'd like to sell.")
        code = input("Enter the stock code you want to purchase: ")
        shares = get_valid_input("How many shares would you like to sell? ", range(1, 100000))
        x=0
        try:
            sale_value = calculate_specific_stock_value(code,shares)
            if my_stocks_shares[code] >= shares:
                my_stocks_shares[code] -= shares
                balance += sale_value
                calculate_personal_stock_value()
                show_stocks()
            else:
                print(f"You don't have enough stocks, owned: {my_stocks_shares[code]}, asked: {shares}.")
        except ValueError:
            print("Not such code exists, try again using a valid code!")
        

def main():
    calculate_personal_stock_value()
    global my_stocks_value
    while True:
        choice = display_menu()
        if choice == 1:
            check_balance()
        elif choice == 2:
            purchase_stocks()
        elif choice == 3:
            advance_day()
        elif choice == 4:
            sell_stock()
        elif choice == 5:
            print("Goodbye!")
            break

if __name__ == "__main__":
    print("Welcome to the Stock Exchange Game!")
    print("Day: ",turn)
    main()