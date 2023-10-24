#Tic-Tac-Toe

import random
from time import sleep

Q = 3

def rules():
    """Shows the rules."""
    
    print("\nThe goal of the game is to line up 3(three) X marks in a row")
    sleep(1)
    print("\nIt can be horizontally, vertically or diagonally.")
    sleep(1)
    main()


def close():
    """Exits the program after entering any key."""

    while True:
        exit_keyword=input("\nEnter any key to exit:   ")
        if exit_keyword!="":
            exit()


def printer(board):
    """Formats and displays the board."""

    for row in range(Q):
        for column in range(Q):
            if column == (Q - 1):
                mark = board[row][column]
                print(f"{mark:^3}", end = " ")
            else:
                mark = board[row][column]
                print(f"{mark:^3} |", end=" ")
        print(" ")
        if row != (Q - 1):
            print("-" * (Q * 5))


def pc_turn(board, move):
    """What happens during the player's turn."""

    player_row = None
    player_column = None
    player_move_list = list(move)

    if player_move_list[0].lower() == "a":
        player_row=0
    elif player_move_list[0].lower() == "b":
        player_row=1
    elif player_move_list[0].lower() == "c":
        player_row=2

    if player_move_list[1] == "1":
        player_column=0
    elif player_move_list[1] == "2":
        player_column=1
    elif player_move_list[1] == "3":
        player_column=2

    if board[player_row][player_column] == "X" or board[player_row][player_column] == "O":
        print("That slot has already been uses\n")
        sleep(0.85)
        printer(board)
    else:
        board[player_row][player_column] = "X"
        sleep(0.85)
        printer(board) 


def npc_turn(board):
    """What happens during the NPC's turn."""

    while True:
        rows = range(Q)
        columns = range(Q)
        npc_row = random.choice(rows)
        npc_column = random.choice(columns)

        if board[npc_row][npc_column] != "X" and board[npc_row][npc_column] != "O":
            board[npc_row][npc_column] = "O"
            printer(board)
            break


def check_for_rows(board):
    """Checks for a win in every row."""

    for row in range(Q):
        cross_counter = 0
        circle_counter = 0
        for column in range(Q):
            if board[row][column] == "X":
                    cross_counter += 1
                    if cross_counter == 3:
                        print("You won!!")
                        close()
            elif board[row][column] == "O":
                    circle_counter += 1
                    if circle_counter == 3:
                        print("You lost!!")
                        close()


def check_for_columns(board):
    """Checks for a win in every column."""

    for column in range(Q):
        cross_counter = 0
        circle_counter = 0
        for row in range(Q):
            if board[row][column] == "X":       
                    cross_counter += 1
                    if cross_counter == 3:
                        print("You won!!")
                        close()
            elif board[row][column] == "O":
                    circle_counter += 1
                    if circle_counter == 3:
                        print("You lost!!")
                        close()


def check_for_diagonals(board):
    if (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") or (board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X"):
        print("You won!!")
        close()
    elif (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O") or (board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "O"):
        print("You lost!!")
        close()


def check_for_draw(board):
    """Checks for a draw."""

    used_slots=0
    for row in range(Q):
        for column in range(Q):
            if board[row][column] == "X" or board[row][column] == "O":     
                    used_slots += 1
                
    if used_slots == (Q ** 2):
        print("It's a draw!!")
        close()


def board_generator():
    """Generates the playing board(dynamic)."""
    
    board=[]
    for row in range(Q):
        row=[]
        for column in range(Q):
            row.append("")
        board.append(row)
    return board


def main():
    """Main function that houses the structure and logic of the program."""
    
    player_choice = input("\nStart -> 1\nRules -> 2\nExit -> 3   ")
    if player_choice == "1": #Creación del tablero
        board = board_generator()
        printer(board)
        while True:
            move=input("\nRules -> 2\nExit -> 3\nRows: A, B, C\nColumns: 1, 2, 3\nEnter row & column:   ")
            if move=="2":
                rules()
            elif move=="3":
                close()
            else:
                pc_turn(board, move)
                check_for_rows(board)
                check_for_columns(board)
                check_for_diagonals(board)
                check_for_draw(board)
                print("\n--- NPC's Turn: ---\n")
                sleep(1)
                npc_turn(board)
                check_for_rows(board)
                check_for_columns(board)
                check_for_diagonals(board)
                check_for_draw(board)
    elif player_choice=="2":
        rules()
    elif player_choice=="3":
        close()

main()
