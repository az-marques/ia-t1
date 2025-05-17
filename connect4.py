from state import State
import minmax

#cada vetor de pesos deve ter 8 números reais
def torneio(pesos1, pesos2):
    board = [[' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ']]
    
    state = State(board, True)
    player_to_move = 1

    while (not state.is_terminal()):
        
        if player_to_move == 1:
            minmax.eval_values = pesos1
            move = minmax.alpha_beta_search(state)
            
            state = state.action(move)
            player_to_move = 2
        elif player_to_move == 2:
            minmax.eval_values = pesos2
            move = minmax.alpha_beta_search(state)

            state = state.action(move)
            player_to_move = 1

    return state.is_terminal()

def jogo():
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
        
        print("Legal Moves: " + str(state.legal_moves()) + "(Suggested " + str(minmax.alpha_beta_search(state)) + ")")
        move = int(input("Enter legal move:"))
        while (not (move in state.legal_moves())):
            move = int(input("Illegal move! Enter legal move:"))

        if player_to_move == 1:
            state = state.action(move)
            player_to_move = 2
        elif player_to_move == 2:
            state = state.action(move)
            player_to_move = 1

    print()
    state.print_board()
    if (state.is_terminal() == 1):
        print("Player 1 wins!")
    elif (state.is_terminal() == 2):
        print("Player 2 wins!")
    else:
        print("Tie!")

if __name__ == "__main__":
    minmax.eval_values = [-0.05110778,  0.68812556,  0.9629372,  -0.00359001,  1.15666125,  0.25216188, 0.50922503, -0.32421343]
    jogo()