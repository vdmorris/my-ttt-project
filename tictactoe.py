'''
Assignment: Tic-Tac-Toe
Author: Vanessa Morris-Cartagena
'''

def main():
        player = swap("")
        board = create()
        while not (check_win(board) or player_tie(board)):
            draw(board)
            input_move(player, board)
            player = swap(player)
        draw(board)
        print("Thanks for playing! Play again!") 

def create():
    board = []
    for cell in range(9):
        board.append(cell + 1)
    return board

def draw(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('<>-<>')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('<>-<>')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def player_tie(board):
    for cell in range(9):
        if board[cell] != "x" and board[cell] != "o":
            return False
    return True

def input_move(player, board):
    cell = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[cell - 1] = player

def check_win(board):
    return (board[0] == board[1] == board[2] or
    board[3] == board[4] == board[5] or
    board[6] == board[7] == board[8] or
    board[0] == board[3] == board[6] or
    board[1] == board[4] == board[7] or
    board[2] == board[5] == board[8] or
    board[0] == board[4] == board[8] or
    board[2] == board[4] == board[6])


def swap(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"


if __name__ == "__main__":
    main()
