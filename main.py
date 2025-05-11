from state import State
import minmax

def connect4_jogo():
    board = [[' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ']]
    
    state = State(board, True)
    player_to_move = 1

    while (not state.is_terminal()):
        print()
        state.print_board()
        
        print("Legal Moves: " + str(state.legal_moves()) + "(Suggested " + str(minmax.random_move(state)) + ")")
        move = int(input("Enter legal move:"))
        while (not (move in state.legal_moves())):
            move = int(input("Illegal move! Enter legal move:"))

        if player_to_move == 1:
            state = state.action(move, state.p1_char)
            player_to_move = 2
        elif player_to_move == 2:
            state = state.action(move, state.p2_char)
            player_to_move = 1

    print()
    state.print_board()
    if (state.is_terminal() > 0):
        print("Player 1 wins!")
    elif (state.is_terminal() < 0):
        print("Player 2 wins!")
    else:
        print("Tie!")
        



if __name__ == "__main__":
    connect4_jogo()