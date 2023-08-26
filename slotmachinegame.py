import random
from transpose2dlist import *
import numpy as np

#values are iniialized to make program dynamic

MAX_LINES=3
MIN_BET=1
MAX_BET=100

ROWS=3
COLS=3

win_symbol=[]
bet_amounts=[]
win_amount=0

balance=None

symbols = {
    "#":3,
    "&":5,
    "@":7,
    "$":9,
    "★":1
}

bet_multiplier = {
    "#":8,
    "&":6,
    "@":4,
    "$":2,
    "★":10
}

def slot_machine_outcome():
    all_symbols = []

    #.items() creates an object from a dictionary which segregates key and value
    for key, value in symbols.items():
        for _ in range(value):
            all_symbols.append(key)

    #print(symbols.items())
    #print(all_symbols) 
    cols_of_reels =[]

    #refer matrix.py file
    for i in range(COLS):
        reel=[]
        #copy is created at the satrt of every column to ensure each element does not print more than the max probablity
        current_symbols=all_symbols.copy()

        for j in range(ROWS):
            value=random.choice(all_symbols)
            reel.append(value)
            current_symbols.remove(value)

        cols_of_reels.append(reel)

    return cols_of_reels

#output 2d list will be like => cols_of_reels=[[★,@,$],[#,★,$],[@,★,@]]
#which can be represented in the matrix format like =>
#cols_of_reels=[[★,@,$],
#               [#,★,$],
#               [@,★,@]]
#but since we want the output to be vertical we will transpose this 2d list




def check_winnings(slot_output, lines, total_bet, balance):
    FLAG=0
    
    for i in range(3):
        global symbol_to_check
        symbol_to_check=slot_output[i][0]

        #looping and checking in the first element of the list i.e. 1st list inside the outer list
        for j in range(1,3):
            #print(f"checking >{symbol_to_check}< with element at [{i},{j}] i.e. >{slot_output[i][j]}<")
                    
            if symbol_to_check!=slot_output[i][j]:
                #print(f"all 3 elements not same in row number {i}")
                break
        else:
            FLAG+=1

            # here if multiple lines won then we are appending the win symbol of the lines
            global win_symbol
            win_symbol.append(slot_output[i][0])
            #print(win_symbol)
            
    
    print("==========================================================")
    


    if FLAG>=lines:
        
        #here if mulitple lines are won then we are averaging the symbol value
        for symbol in win_symbol:
            global bet_amounts
            bet_amounts.append(bet_multiplier[symbol])
        #print(bet_amounts)
        
        bet_multiplier_value=int(np.average(bet_amounts))
        #print(bet_multiplier_value)
        win_amount=int(total_bet*bet_multiplier_value)
        print(f"congrats! you won = ${win_amount}")

        if balance==None:
            balance=0

        balance=balance+win_amount
        print(f"current balance = ${balance}") 
    else:
        print("you lost, better luck next time")
        print(f"current balance = ${balance}")

    return balance
         


def amount():
    while True:
        print(f"current balance = ${balance}")
        amount=input("enter the deposit amount $")
        if amount.isdigit():
            if int(amount) > 0:
                break
            else:
                print("enter amount above $0")
        else:
            print("enter a valid amount")
    return amount




def get_no_of_lines():
    while True:
        lines=input(f"enter the bet lines (1-{MAX_LINES}) ")
        if lines.isdigit():
            if 1<= int(lines) <= 3:
                break
            else:
                print(f"enter a number between 1 and {MAX_LINES}")
        else:
            print("enter a valid number")
    return lines     





def get_bet():
    while True:
        amount=input("enter the amount you want to bet on each line $")
        if amount.isdigit():
            if MIN_BET <= int(amount) <= MAX_BET:
                break
            else:
                print(f"bet amount must me between {MIN_BET} and {MAX_BET}")
        else:
            print("enter a valid amount")
    return amount





def main():

    while True:
        
        print("==========================================================")
        print("==========================================================")
        print("####################slot machine game#####################")
        print("==========================================================")
        print("==========================================================")
        #print(f"current balance =${balance_amount}")

        global balance
        
        if balance==None:
            balance=0
        
        balance=int(amount())+balance
        #balance_amount=balance+win_amount
        lines=int(get_no_of_lines())

        while True:
            global bet
            bet = int(get_bet())
            total_bet = bet*lines
            if total_bet>balance:
                print(f"insufficient balance, current balance is ${balance}")
            else:
                
                break
        balance=balance-total_bet
        print("==========================================================")
        print(f"total_bet_placed = ${total_bet} on {lines} lines, remaining balance = ${balance}")
        print("==========================================================")

        slot_output=slot_machine_outcome()  

        #print(slot_output)
        #print("==========================================================")
        
        slot_output=transpose(slot_output)
        print(np.matrix(slot_output))
        #print(slot_output)
        
        #for trying the check_winnings() logic
        # print("==========================================================")
        #here you can rig the outcome
        # slot_output[0][0]="★"
        # slot_output[0][1]="★"
        # slot_output[0][2]="★"
        # slot_output[1][0]="$"
        # slot_output[1][1]="$"
        # slot_output[1][2]="$"
        # slot_output[2][0]="★"
        # slot_output[2][1]="★"
        # slot_output[2][2]="★"
        # print(np.matrix(slot_output))
        
        balance=check_winnings(slot_output,lines,total_bet,balance)
        #print("==========================================================")
        #print(f"previous_balance =${balance}")


if __name__=="__main__":
    main()