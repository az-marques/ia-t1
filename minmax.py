# s0 is empty board - max node
# possible moves are [0-4] unless column is full
# funcao de avaliacao:
# (a * n° linhas abertas) +
# (b * n° de trincas) +
# (c * n° de peças no centro)
from state import State
import random

#for testing
def random_move(state: State):
    return random.choice(state.legal_moves())

def alpha_beta_search(state):
    value, move = max_value(state, float('-inf'), float('inf'), 0)
    return move

def max_value(state: State, alpha, beta, depth):
    if is_cutoff(state, depth):
        return eval(state), None
    
    utility =  float('-inf')
    action = None
    for hypothetical_action in state.legal_moves():
        utility2, action2 = min_value(state.action(hypothetical_action), alpha,beta, depth+1)
        if utility2 > utility:
            utility =  utility2
            action = hypothetical_action
            alpha =  max(alpha, utility)
        #cuts off search
        if utility >= beta:
            return utility, action
    return utility, action


def min_value(state: State, alpha, beta, depth):
    if is_cutoff(state, depth):
        return eval(state), None
    
    utility =  float('inf')
    action = None
    for hypothetical_action in state.legal_moves():
        utility2, action2 = max_value(state.action(hypothetical_action), alpha,beta, depth+1)
        if utility2 < utility:
            utility =  utility2
            action = hypothetical_action
            beta =  min(beta, utility)
        #cuts off search
        if utility <= alpha:
            return utility, action    
    return utility, action

#PLACEHOLDER is cutoff function
def is_cutoff(state: State, depth):
    if state.is_terminal() or depth > 3:
        return True
    return False

#PLACEHOLDER eval function
def eval(state: State):
    return max([state.longest_h_line(state.p1_char),
         state.longest_v_line(state.p1_char),
         state.longest_d_up_line(state.p1_char),
         state.longest_d_down_line(state.p1_char),])