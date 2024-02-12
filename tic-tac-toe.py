""" Morpion game also know as tic-tac-toe. This program uses a random bot 
    to fight the player :) """ 


import random

arr = [' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ']

# Show board function
def show_board():
    print("     4       5       6   ")
    print("         |      |       ")
    print(f"1    {arr[1]}   |   {arr[2]}  |   {arr[3]}")
    print("         |      |       ")
    print("  -------|------|------- ")
    print("         |      |       ")
    print(f"2    {arr[4]}   |   {arr[5]}  |   {arr[6]}")
    print("         |      |       ")
    print("  -------|------|------- ")
    print("         |      |       ")
    print(f"3    {arr[7]}   |   {arr[8]}  |   {arr[9]}")
    print("         |      |       ")

# Check for win function
def check_for_win():
    # Win cases 
    # Lines 
    if arr[1] == arr[2] == arr[3] and arr[3] != ' ':
        if arr[3] == "X":
            return (1, "X")
        else:
            return (1, "0")
    elif arr[4] == arr[5] == arr[6] and arr[6] != ' ':
        if arr[6] == "X":
            return (1, "X")
        else:
            return (1, "0")
    elif arr[7] == arr[8] == arr[9] and arr[9] != ' ':
        if arr[9] == "X":
            return (1, "X")
        else:
            return (1, "0")
    # Rows 
    elif arr[1] == arr[4] == arr[7] and arr[7] != ' ':
        if arr[7] == "X":
            return (1, "X")
        else:
            return (1, "0")
    elif arr[2] == arr[5] == arr[8] and arr[8] != ' ':
        if arr[8] == "X":
            return (1, "X")
        else:
            return (1, "0")
    elif arr[3] == arr[6] == arr[9] and arr[9] != ' ':
        if arr[9] == "X":
            return (1, "X")
        else:
            return (1, "0")
    # Diagonals 
    elif arr[1] == arr[5] == arr[9] and arr[9] != ' ':
        if arr[9] == "X":
            return (1, "X")
        else:
            return (1, "0")
    elif arr[3] == arr[5] == arr[7] and arr[7] != ' ':
        if arr[7] == "X":
            return (1, "X")
        else:
            return (1, "0")
    
    # Game over
    over = True
    for j in arr:
        if j == ' ':
            over = False
            break
    
    # Returns 
    if over == True:
        return (-1, 1)
    else:
        return (0, 1)

# Game start
print("***************************\n")
print("       TIC-TAC-TOE\n")
print("***************************")

# Player's symbol 
print("\nSymbols: \n1- X\n2- 0")
player = int(input("Chose your symbol using 1 or 2: "))

# Error handling
while(player != 1 and player != 2):
    print("Invalid Value ")
    player= int(input("Chose your symbol using 1 or 2: "))

if player == 1:
    player_symbol = "X"
    bot_symbol = "0"
else: 
    player_symbol = "0"
    bot_symbol = "X"

# Starting 
i = 0
while i == 0:
    show_board()
    
    # Player's turn
    invalid = True
    while invalid:
        choice = input("Play: ") 
        if choice == "14" and arr[1] == ' ':
            arr[1] = player_symbol
            invalid = False
        elif choice == "15" and arr[2] == ' ':
            arr[2] = player_symbol
            invalid = False
        elif choice == "16" and arr[3] == ' ':
            arr[3] = player_symbol
            invalid = False
        elif choice == "24" and arr[4] == ' ':
            arr[4] = player_symbol
            invalid = False
        elif choice == "25" and arr[5] == ' ':
            arr[5] = player_symbol
            invalid = False
        elif choice == "26" and arr[6] == ' ':
            arr[6] = player_symbol
            invalid = False
        elif choice == "34" and arr[7] == ' ':
            arr[7] = player_symbol
            invalid = False
        elif choice == "35" and arr[8] == ' ':
            arr[8] = player_symbol
            invalid = False
        elif choice == "36" and arr[9] == ' ':
            arr[9] = player_symbol
            invalid = False
    show_board()
    (i, symbol) = check_for_win()

    # bot turn
    bot = random.randint(1, 9)
    # Looking for blank
    while arr[bot] != " ":
        bot = random.randint(1, 9)
    arr[bot] = bot_symbol
    show_board()
    (i, symbol) = check_for_win()
    
# Check for game situation
if i == 1:
    if symbol == player_symbol:
        print("You won")
    else:
        print("You lost")
elif i == -1: 
    print("Game Over")
