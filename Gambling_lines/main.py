import random #this is how we import modules

#static Variables
MAX_LINES = 3 #convention in Python all capitalised names are static variables that cant be changed
MAX_BET= 100
MIN_BET= 1
#ROWS and columns in the slot machine
ROWS= 3
COLS=3

symbol_count = { #the number of symbols that would be in the slot machine 
    "A":2,
    "B":4,
    "C":6,
    "D":8,
}# this is just a good coding scheme, if we would have made a list we would have to manually add new symbols
symbol_Value= {
    "A":5,
    "B":4,
    "C":2,
    "D":1,
}

def check_winnings(columns,lines, bet, values):
    winnings =0 
    winning_lines = []
    for line in range(lines):
        symbol= columns[0][lines]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet 
            winning_lines.append(lines+1)
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    #below function add all the symbols to the list
    for symbol, symbol_count in symbols.items(): # .items we had to itterate over a dictionary this is how we can select the key value pairs that we want to itterate over a dictionary
        for _ in range(symbol_count):#_ anonymous variables loop thorugh something we dont care looping over, ignore unsused variables
            all_symbols.append(symbol)#we had just put all the A/B/C/D in the all symbol list

    columns= [] #this usually represents rows but here it is for the first column
    for _ in range(cols):
        column= [] #find the column list which is empty
        current_symbols = all_symbols[:]#slicing operator the copy will not have the same changes as the previous other wise its a reference 
        for _ in range(rows):
            value = random.choice(current_symbols) #so we don't select the already selected value again
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def print_slot_machine(columns):
    #transposing a matrix needs to be done 
    for row in range(len(columns[0])):#promise there will be one column always
        for i,column in enumerate (columns): #enumerate gives the index value of the column to loop thorough
            if i!= len(columns) -1:
                print(column[row], end=" | ")#we dont need pipe operator after the third column element so we enumerate
            else:
                print(column[row],end="")# so we don't change the line
        
        print() #bring it to next line
def deposit(): #collecting user input, it is a function
    while True:
        amount = input("Amount you would like to deposit: ")
        if amount.isdigit(): #method that can be used to check if the given digit is a num 
            amount=int(amount) #typecasting the amount to int
            if amount > 0:
                break
            else: 
                print("Please enter a number greater than 0") 
        else: 
            print("Please enter a number: ")
    return amount

def get_number_of_lines(): #
    while True:
        lines = input("Number of lines you would like to bet on (1-"+ str(MAX_LINES)+ ")? ") 
        if lines.isdigit(): #method that can be used to check if the given digit is a num 
            lines=int(lines) #typecasting the amount to int
            if 1<=lines<=MAX_LINES:
                break
            else: 
                print("Enter a valid number of lines") 
        else: 
            print("Please enter a number: ")
    return lines

def get_bet():
    while True:
        amount = input("How much would You like to bet on each line: ") 
        if amount.isdigit(): #method that can be used to check if the given digit is a num 
            amount=int(amount) #typecasting the amount to int
            if MIN_BET<=amount<=MAX_BET:
                break
            else: 
                print(f"amount must be between {MIN_BET} and {MAX_BET}")#we used a fstring to get some variables printed 
        else: 
            print("Please enter a number: ")
    return amount

def spin(balance):
    lines= get_number_of_lines()

    while True:#while loop is added here to ensure the balance is is sufficient 
        bet=get_bet()
        total_bet= bet* lines

        if total_bet> balance:
            print(f"Not enough balance to make the bet, Your current balance is {balance}")
        else:
            break 

    print(f"you are betting {bet} on {lines}lines. Total bet amount is {bet * lines}")
    #print(balance,lines)
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines= check_winnings(slots, lines, bet, symbol_Value)
    print(f"You won: ${winnings}")
    print(f"You won on lines, ", *winning_lines)
    return winnings - total_bet

def main(): #if the game end we can call this function an everything will restart
    balance=deposit() #this is how we can call function
    while True:
        print(f"Current balance is ${balance}")
        answer = input("press enter to play (q to quit)")
        if answer == 'q':
            break #
        balance += spin(balance)

    print(f"You left with ${balance}")
main()
