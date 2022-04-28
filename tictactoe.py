def main():
        player = swap_player("")
        board = create_board()
        show_board(board)
        print("Good game. Thanks for playing!") 

def create_board():
    board = []
    return board

def show_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-<>-<>-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-<>-<>-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def player_draw(board):
    for cell in range(9):
        if board[cell] != "x" and board[cell] != "o":
            return False
    return True

def input_move(player, board):
    cell = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[cell - 1] = player

def check_win(board):
     return ""
    

def swap_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"


if __name__ == "__main__":
    main()