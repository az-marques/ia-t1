from state import State

eval_values = [1.0, #player longest_line weight
               1.0, #player line_len weight
               1.0, #player n_lines weight
               1.0, #player center_pieces weight
               -1.0, #opponent longest_line weight
               -1.0, #opponent avg_line_len weight
               -1.0, #opponent n_lines weight
               -1.0,] #opponent center_pieces weight

eval_player = 0

def alpha_beta_search(state: State):
    global eval_player 
    if state.to_move:
        eval_player = 1
    else:
        eval_player = 2
    value, move = max_value(state, float('-inf'), float('inf'), 0)
    return move

def max_value(state: State, alpha, beta, depth):
    cutoff, terminal = is_cutoff(state, depth)
    if cutoff:
        return eval(state, terminal), None
    
    utility =  float('-inf')
    action = None
    for hypothetical_action in state.legal_moves():
        utility2, action2 = min_value(state.action(hypothetical_action), alpha,beta, depth+1)
        if utility2 >= utility:
            utility =  utility2
            action = hypothetical_action
            alpha =  max(alpha, utility)
        #cuts off search
        if utility >= beta:
            return utility, action
    return utility, action


def min_value(state: State, alpha, beta, depth):
    cutoff, terminal = is_cutoff(state, depth)
    if cutoff:
        return eval(state, terminal), None
    
    utility =  float('inf')
    action = None
    for hypothetical_action in state.legal_moves():
        utility2, action2 = max_value(state.action(hypothetical_action), alpha,beta, depth+1)
        if utility2 <= utility:
            utility =  utility2
            action = hypothetical_action
            beta =  min(beta, utility)
        #cuts off search
        if utility <= alpha:
            return utility, action    
    return utility, action

#PLACEHOLDER is cutoff function
def is_cutoff(state: State, depth):
    terminal = state.is_terminal()
    if terminal or depth >= 3:
        return True, terminal
    return False, None

def eval(state: State, terminal):
    if terminal:
        if eval_player == 1 and terminal == 1:
            return float('inf')
        if eval_player == 1 and terminal == 2:
            return float('-inf')
        if eval_player == 1 and terminal == 3:
            return 0
        if eval_player == 2 and terminal == 2:
            return float('inf')
        if eval_player == 2 and terminal == 1:
            return float('-inf')
        if eval_player == 2 and terminal == 3:
            return 0
        

    p1_longest_line = max([state.longest_h_line(state.p1_char),
                           state.longest_v_line(state.p1_char),
                           state.longest_d_up_line(state.p1_char),
                           state.longest_d_down_line(state.p1_char),])
    p1_longest_line = min(p1_longest_line, 4) #no benefit to line longer than 4 - a game ending with a 5 line is not a "better" win
    p1_n_lines, p1_avg_line_len = state.line_stats(state.p1_char)
    p1_center_pieces = state.center_pieces(state.p1_char)

    p2_longest_line = max([state.longest_h_line(state.p2_char),
                           state.longest_v_line(state.p2_char),
                           state.longest_d_up_line(state.p2_char),
                           state.longest_d_down_line(state.p2_char),])
    p2_longest_line = min(p2_longest_line, 4) #no benefit to line longer than 4 - a game ending with a 5 line is not a "better" win
    p2_n_lines, p2_avg_line_len = state.line_stats(state.p2_char)
    p2_center_pieces = state.center_pieces(state.p2_char)

    if eval_player == 1:
        return (eval_values[0]*p1_longest_line +
                eval_values[1]*p1_avg_line_len +
                eval_values[2]*p1_n_lines + 
                eval_values[3]*p1_center_pieces +

                eval_values[4]*p2_longest_line +
                eval_values[5]*p2_avg_line_len +
                eval_values[6]*p2_n_lines +
                eval_values[7]*p2_center_pieces)
    else:
        return (eval_values[0]*p2_longest_line +
                eval_values[1]*p2_avg_line_len +
                eval_values[2]*p2_n_lines + 
                eval_values[3]*p2_center_pieces +

                eval_values[4]*p1_longest_line +
                eval_values[5]*p1_avg_line_len +
                eval_values[6]*p1_n_lines +
                eval_values[7]*p1_center_pieces)
    