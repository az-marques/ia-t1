import connect4
import pygad #pip3 install pygad
import random
import numpy

        
def fitness_function(ga_instance, solution, solution_idx):
        
    wins = 0
    games = 100
    for i in range(games//2):
        #play against a random non-evolving agent
        result = connect4.torneio(solution, [random.random() for i in range(4)] + [(-1* random.random()) for i in range(4)])
        if result == 1: #win
            wins = wins + 2
        elif result == 3: #draw, worth half a win
            wins = wins + 1

        #again, but this time go second
        result = connect4.torneio([random.random() for i in range(4)] + [(-1* random.random()) for i in range(4)], solution)
        if result == 2: #win
            wins = wins + 2
        elif result == 3: #draw, worth half a win
            wins = wins + 1
    
    winrate =  (wins/2) / games
    #print(str(winrate*100) + "%", end=" ")
    #sprint(solution)
    return winrate

def parent_selection_tournament(fitness, num_parents, ga_instance: pygad.GA):
    
    #get the n best performing individuals this generation, where n twice the number of parents we need
    num_competitors = num_parents*2
    fitness_sorted = sorted(range(len(fitness)), key=lambda k: fitness[k])
    fitness_sorted.reverse()
    best_performers = numpy.empty((num_competitors, ga_instance.population.shape[1]))
    for i in range(num_competitors):
        best_performers[i, :] = ga_instance.population[fitness_sorted[i], :].copy()

    #have them fight in a round robin tournament
    wins = [0 for i in range(num_competitors)]
    match_ordering = list(range(num_competitors))
    for rr_round in range((num_competitors-1)):
        for i in range(num_parents): #num_competitors//2
            p1 = match_ordering[i]
            p2 = match_ordering[-(i+1)]
            result = connect4.torneio(best_performers[p1], best_performers[p2])
            if result == 1:
                wins[p1] = wins[p1] + 2
            elif result == 2:
                wins[p2] = wins[p2] + 2
            elif result == 3:
                wins[p1] = wins[p1] + 1
                wins[p2] = wins[p2] + 1
        minus_fixed = match_ordering[1:]
        match_ordering = [match_ordering[0]] + minus_fixed[-1:] + minus_fixed[:-1] #round robin circle method

    parents = numpy.empty((num_parents, ga_instance.population.shape[1]))
    parent_ids = numpy.empty(num_parents, int)
    wins_sorted =  sorted(wins, reverse=True)
    for i in range(num_parents):
        parent_index = wins.index(wins_sorted[i]) #index of i-th best scoring parent
        parents[i,:] = best_performers[parent_index]
        parent_ids[i] = fitness_sorted[parent_index]

    print("Generation "+str(ga_instance.generations_completed)+" completed, best fitness "+str(max(fitness)))

    return parents, parent_ids
        
        

if __name__ == "__main__":
    ga_instance = pygad.GA(num_generations=20,
                       num_parents_mating=5,
                       fitness_func=fitness_function,
                       sol_per_pop=30,
                       num_genes=8,
                       init_range_low=-1,
                       init_range_high=1,
                       parent_selection_type=parent_selection_tournament,
                       keep_parents=-1,
                       crossover_type="single_point",
                       crossover_probability=0.5,
                       mutation_type="random",
                       mutation_probability=0.1,)
    
    ga_instance.run()
    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    print("Parameters of the best solution : {solution}".format(solution=solution))
    print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
    ga_instance.plot_fitness()

