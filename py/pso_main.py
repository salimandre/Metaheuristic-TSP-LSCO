from benchmark_toolbox import *
import time

tic=time.time()
all_cost, all_pos, ind_best=solve_with_pso(func_name='Shifted Griewank', dim=500, n_particles=5000, n_iters=250, inertia=0.8, cognitive=0.4, social=0.3, n_runs=10, plot_cost=True)
toc=time.time()

print('\n\t***** RESULTS OUT OF '+str(len(all_cost))+' *****\t\n')
print('comput. time: ',(toc-tic)/25,'s')
print('best cost: ', all_cost[ind_best])
print('median cost: ', np.median(all_cost))
print('avg cost: ', np.mean(all_cost))
print('best pos: ',all_pos[ind_best])
print('\n\t*****************\t\n')

#random_search_pso(func_name='Shifted Sphere', dim=50, n_particles=1000, n_iters=250, inertia=(0.6,0.7,0.8,0.9), cognitive=(0.1,0.2,0.3,0.4,0.5), social=(0.1,0.2,0.3,0.4,0.5), n_selection_iters=10)


