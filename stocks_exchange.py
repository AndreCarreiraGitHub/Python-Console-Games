from config import RED, GREEN, YELLOW, BLUE, MAGENTA, RESET
import pandas as pd

stock_data = pd.read_csv("stock_exchange/stock.csv")
balance_data = pd.read_csv("stock_exchange/balance.csv")
my_stocks = None

balance = balance_data.iat[0,0]
stock_rows = stock_data.shape[0]

def ask_user_action(answer):
    if answer != "quit":
        answer = int(answer)
        while answer != 1 and answer != 2 and answer != 3:
            if answer != 1 and answer != 2 and answer != 3:
                print("\nPlease write a valid input.")
                answer = input("You: ")
    return answer

def check_balance(balance, my_stocks):
    print("\n£",balance)
    print("These are your stocks: \n", my_stocks)

def check_stock_change(x,stock_data):
    data = False
    previous = float(stock_data.iat[x,3])
    current = float(stock_data.iat[x,4])
    if current > previous:
        data = True
    return data

def show_every_stock(stock_rows,stock_data):
    y=0
    change_stock=False
    for x in range(stock_rows):
        stock_name = stock_data.iat[y,0]
        stock_code = stock_data.iat[y,1]
        stock_price = stock_data.iat[y,4]
        change_stock = check_stock_change(x,stock_data)
        if change_stock == True:
            print(f"\n{GREEN}{stock_name}{RESET}",f"{MAGENTA}{stock_code}{RESET}",f"{YELLOW}{stock_price}{RESET}")
        else:
            print(f"\n{RED}{stock_name}{RESET}",f"{MAGENTA}{stock_code}{RESET}",f"{YELLOW}{stock_price}{RESET}")
        y+=1

def purchase_stocks(stock_purchase_code,stock_purchase_shares,stock_data,stock_rows):
    y=0
    for x in range(stock_rows):
        stock_code = stock_data.iat[y,1]
        if stock_purchase_code == stock_code:
            print("Found Match!")
        else:
            print("No Match Found...")
        y+=1





turn = 1    
print("\nTurn: ",turn,"\n")

print("\nWhat's your name?")
name = input("You: ")

answer = ""
display_answer = ""
stock_answer = ""
stock_purchase_code = ""
stock_purchase_shares = ""

while answer != "quit":
    print("\n",name," what would you like to do today?\n")
    print("View Balance: 1\nView Stock Market: 2\nOr Advance a Day: 3\n")

    answer = input("You: ")
    answer = ask_user_action(answer)
    
    if answer == 1:
        check_balance(balance, my_stocks)
    elif answer == 2:
        print("\nWould you like for every stock available to be displayed (1), or a specific stock? (2).\n")
        display_answer = input("You: ")
        display_answer = ask_user_action(display_answer)
        while display_answer == 3:
            if display_answer == 3:
                display_answer = ask_user_action(display_answer)
        if display_answer == 1:
            show_every_stock(stock_rows,stock_data)
            print("\nIs there any you would like to invest in?\nYes: 1\nNo: 2")
            stock_answer = input("You: ")
            stock_answer = ask_user_action(stock_answer)
            while stock_answer == 3:
                if stock_answer == 3:
                    stock_answer = ask_user_action(stock_answer)
            if stock_answer == 1:
                print("\nWhich stock do you want to get? (type stock code)")
                stock_purchase_code = input("You: ")
                print("And how many shares would you like?")
                stock_purchase_shares = input("You: ")
                purchase_stocks(stock_purchase_code,stock_purchase_shares,stock_data,stock_rows)