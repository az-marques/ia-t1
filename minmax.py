# s0 is empty board - max node
# possible moves are [0-4] unless column is full
# funcao de avaliacao:
# (a * n° linhas abertas) +
# (b * n° de trincas) +
# (c * n° de peças no centro)# (c * n° de peças no centro)
from state import State
import random

#for testing
def random_move(state: State):
    return random.choice(state.legal_moves())
