# Metaheuristic Assignment

## Large Scale Continuous Optimization

As we wanted to see how well perform **Particle Swarm Optimization** on different objective functions and in different dimension settings we only used this one algorithm. We used the library **Pyswarms** for PSO evaluations.

For dim 50 we used a budget of 250K evaluations and for dim 500 a budget of 1.25M evaluations. We chose our cognitive, social and inertia parameters by performing a **random search** among 100 settings and each setting was evaluated 10 times on the Shifted Sphere function in dim 50. We kept these same parameters for every other computations. 

In dim 50 we tried two settings 1000 particles with 250 iterations and 5000 particles with 50 iterations. The latter proved to be better on Sphere and Rosenbrock functions. In dim 500 we tried the following two settings: 5000 particles with 250 iterations and 10000 particles with 100 iterations but they provided similar results.

We could observ the **curse of dimensionality**. For Rosenbrock and Sphere the domain is [-100, 100]^D whose volume increases exponentially with the dimension plus the sphere function tends to become shaper and sharper. Hence for some of the functions and domains it requires more and more ressources as the dimension increases to achieve good results. Results could have been improved by taking more particles but it is expensive in RAM and leads to matrix computations in high dimension. The library we used was not suited for that. Although Pyswarms was able to handle boundary constraints. 

| Code CEC’08 | Name | Dim | Bounds | Min. Value | Algo | Particles | Iter. | Evals | Stop. Criteria | Cognitive | Social | Inertia | Comput. Time (s) | # runs | Mean Value | Median Value | Best Value | Plot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F1 | Shifted Sphere | 50 | [−100,100] | -450 | PSO | 5000 | 50 | 250K | n_evals | 0.4 | 0.3 | 0.8 | 1.9 | 25 | 5690.8 | 5540.3 | 2512.7 | <img src="/cec2018/sphere/shifted_sphere_pso_50_bis.png" height="50" width="100"> |
| F2 | Shifted Schwefel | 50 | [−100,100] | -450 | PSO | 1000 | 250 | 250K | n_evals | 0.4 | 0.3 | 0.8 | 3.8 | 25 | -399.9 | -400.3 | -407.2 | <img src="/cec2018/schwefel/shifted_schwefel_pso_50.png" height="50" width="100"> |
| F3 | Shifted Rosenbrock | 50 | [−100,100] | 390 | PSO | 5000 | 50 | 250K | n_evals | 0.4 | 0.3 | 0.8 | 6.7 | 25 | 28753075.4 | 19607298.2 | 1771071.4 | <img src="/cec2018/rosenbrock/shifted_Rosenbrock_pso_50_bis.png" height="50" width="100"> |
| F4 | Shifted Rastrigin | 50 | [−5,5] | -330 | PSO | 1000 | 250 | 250K | n_evals | 0.4 | 0.3 | 0.8 | 8.7 | 25 | -3.6 | 1.3 | -87.4 | <img src="/cec2018/rastrigin/shifted_Rastrigin_pso_50.png" height="50" width="100"> |
| F5 | Shifted Griewank | 50 | [−600, 600] | -180 | PSO | 1000 | 250 | 250K | n_evals | 0.4 | 0.3 | 0.8 | 9.8 | 25 | -106.9 | -115.9 | -143.8 | <img src="/cec2018/griewank/shifted_Griewank_pso_50.png" height="50" width="100"> |
| F6 | Shifted Ackley | 50 | [−32,32] | -140 | PSO | 1000 | 250 | 250K | n_evals | 0.4 | 0.3 | 0.8 | 5.7 | 25 | -126.2 | -126.2 | -130.4 | <img src="/cec2018/ackley/shifted_Ackley_pso_50.png" height="50" width="100"> |


| Code CEC’08 | Name | Dim | Bounds | Min. Value | Algo | Particles | Iter. | Evals | Stop. Criteria | Cognitive | Social | Inertia | Comput. Time (s) | # runs | Mean Value | Median Value | Best Value | Plot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F1 | Shifted Sphere | 500 | [−100,100] | -450 | PSO | 5000 | 250 | 1.25M | n_evals | 0.4 | 0.3 | 0.8 | 43.8 | 25 | 1.1e6 | 1.1e6 | 9.5e5 | <img src="/cec2018/sphere/shifted_sphere_pso_500.png" height="50" width="100"> |
| F2 | Shifted Schwefel | 500 | [−100,100] | -450 | PSO | 5000 | 250 | 1.25M | n_evals | 0.4 | 0.3 | 0.8 | 44.0 | 25 | -345.2 | -345.4 | -349.7 | <img src="/cec2018/schwefel/shifted_schwefel_pso_500.png" height="50" width="100"> |
| F3 | Shifted Rosenbrock | 500 | [−100,100] | 390 | PSO | 5000 | 250 | 1.25M | n_evals | 0.4 | 0.3 | 0.8 | 109.3 | 25 | 297e9 | 297e9 | 267e9 | <img src="/cec2018/rosenbrock/shifted_Rosenbrock_pso_500.png" height="50" width="100"> |
| F4 | Shifted Rastrigin | 500 | [−5,5] | -330 | PSO | 5000 | 250 | 1.25M | n_evals | 0.4 | 0.3 | 0.8 | 56.3 | 25 | 6291.7 | 6291.7 | 5791.9 | <img src="/cec2018/rastrigin/shifted_Rastrigin_pso_500.png" height="50" width="100"> |
| F5 | Shifted Griewank | 500 | [−600, 600] | -180 | PSO | 5000 | 250 | 1.25M | n_evals | 0.4 | 0.3 | 0.8 | 21.5 | 25 | 8509.6 | 8456.2 | 8105.1 | <img src="/cec2018/griewank/shifted_Griewank_pso_500.png" height="50" width="100"> |
| F6 | Shifted Ackley | 500 | [−32,32] | -140 | PSO | 5000 | 250 | 1.25M | n_evals | 0.4 | 0.3 | 0.8 | 64.0 | 25 | -119.6 | -119.6 | -119.6 | <img src="/cec2018/ackley/shifted_Ackley_pso_500.png" height="50" width="100"> |

## Discrete Optimization: TSP

During the course I had already implemented my homemade version of genetic algorithm and I had applied it to TSP (https://github.com/salimandre/metaheuristics). This time for a change I chose to go for **Local Search Algorithms** namely 2-swap, 3-swap, 2-opt and a **Greedy Algorithm**. Here I implemented everything myself.

In k-swap at each step we perform a permutation of k cities in the path and we keep it if it decreases the total distance. In k-opt at each step we remove k edges from the path and we add k new edges that we keep if it decreases the total distance. We used also a greedy policy as a baseline and as an initialization. We connect each city with the closest city.

2-opt with greedy policy proved to provide convincing results and in a short amount of time. In order to improve results we could have added some technique such as Simulated Annealing to avoid being stuck to quickly in local minima. Also if we had to deal with larger sized TSP we could have used Kdtree in order to make computations more effective.

### dj38

| Algo | Iters | Stop. Criteria | Comput. Time (s) | # runs | Mean Value | Best Value | Plot |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Greedy | 700 | when Hamiltonian | 0.012 | 10 | 6771.5 | 6771.5 | <img src="/tsp/data/dj38/plots/dj38_greedy_cost.png" height="50" width="50"> |
| 2-swap | 100K | n_iters or when all 2-swap neighbors of graph have been visited | 0.24 | 10| 9978.8 | 8111.6 |<img src="/tsp/data/dj38/plots/dj38_2_swap_cost.png" height="50" width="50"> |
| 2-swap + Greedy | 100K | n_iters or when all 2-swap neighbors of graph have been visited | 0.11 | 10 | 6723.4 | 6664.1 |<img src="/tsp/data/dj38/plots/dj38_2_swap_greedy_cost.png" height="50" width="50"> |
| 3-swap | 100K | n_iters or when all 3-swap neighbors of graph have been visited | 6.75 | 10 | 9349.3 | 7937.7 |<img src="/tsp/data/dj38/plots/dj38_3_swap_cost.png" height="50" width="50"> |
| 3-swap + Greedy | 100K | n_iters or when all 3-swap neighbors of graph have been visited | 4.12 | 10 | 6659.4 | 6659.4 |<img src="/tsp/data/dj38/plots/dj38_3_swap_greedy_cost.png" height="50" width="50"> |
| 2-opt | 10K | n_iters or when all 2-opt neighbors of graph have been visited | 0.1 | 10 | 7353.0 | 6659.4 |<img src="/tsp/data/dj38/plots/dj38_2_opt_cost.png" height="50" width="50"> |
| 2-opt + Greedy | 10K | n_iters or when all 2-opt neighbors of graph have been visited | 0.01 | 10 | 6694.6 | 6664.1 |<img src="/tsp/data/dj38/plots/dj38_2_opt_greedy_cost.png" height="50" width="50"> |

<p align="center">
  <img src="tsp/gif/dj38_2_opt.gif" width="24%">
  <img src="tsp/gif/dj38_3_swap.gif" width="24%">
</p>
<p align="center">
  respectively 2-opt and 3-swap with random initialization applied to dj38
</p>

### qa194

| Algo | Iters | Stop. Criteria | Comput. Time (s) | # runs | Mean Value | Best Value | Plot |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Greedy | 250K | when Hamiltonian | 0.36 | 10 | 12346.9 | 12346.9 |<img src="/tsp/data/qa194/plots/qa194_greedy_cost.png" height="50" width="50"> |
| 2-swap | 250K | n_iters or when all 2-swap neighbors of graph have been visited | 39.7 | 10| 20028.8 | 18409.6 |<img src="/tsp/data/qa194/plots/qa194_2_swap_cost.png" height="50" width="50"> |
| 2-swap + Greedy | 250K | n_iters or when all 2-swap neighbors of graph have been visited | 8.1 | 10 | 11515.8 | 11318.5 |<img src="/tsp/data/qa194/plots/qa194_2_swap_greedy_cost.png" height="50" width="50"> |
| 2-opt | 250K | n_iters or when all 2-opt neighbors of graph have been visited | 32.2 | 10 | 10520.8 | 10108.0 |<img src="/tsp/data/qa194/plots/qa194_2_opt_cost.png" height="50" width="50"> |
| 2-opt + Greedy | 250K | n_iters or when all 2-opt neighbors of graph have been visited | 11.9 | 10 | 10078.4 | 9931.1 |<img src="/tsp/data/qa194/plots/qa194_2_opt_greedy_cost.png" height="50" width="50"> |

<p align="center">
  <img src="tsp/gif/qa194_2_opt_greedy.gif" width="24%">
</p>
<p align="center">
  2-opt with greedy initialization applied to qa194
</p>
