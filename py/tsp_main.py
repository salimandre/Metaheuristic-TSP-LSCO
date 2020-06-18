from tsp_toolbox import *
import matplotlib.pyplot as plt

PATH_DJ38='/Users/mac/Desktop/python/final_meta/data/dj38'
PATH_QA194='/Users/mac/Desktop/python/final_meta/data/qa194'

# ---------------------------------------------------------------

dj38 = TSP(PATH_DJ38)

#dj38.scale_back()

dj38.k_opt_solver(n_iters=10000, display_time=0.01,show_cost=False, init_with='random')

#dj38.k_swap_solver(n_iters=100000, display_time=0.01, show_cost=False, init_with='random', k=3)

#dj38.greedy_solver(display_time=0, show_cost=False)

# ---------------------------------------------------------------

#qa194 = TSP(PATH_QA194)

#qa194.scale_back()

#qa194.greedy_solver(display_time=0, show_cost=True)

#qa194.k_swap_solver(n_iters=250000, display_time=0, show_cost=True, init_with='greedy', k=2)

#qa194.k_opt_solver(n_iters=250000, display_time=0.001,show_cost=False, init_with='greedy')
