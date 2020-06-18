# Metaheuristic Assignment

## Large Scale Continuous Optimization

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

### dj38

| Algo | Iters | Stop. Criteria | Comput. Time (s) | # runs | Mean Value | Best Value | Plot |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Greedy | 700 | when Hamiltonian | 0.012 | 10 | 6771.5 | 6771.5 | |
| 2-swap | 100K | n_iters or when all 2-swap neighbors of graph have been visited | 0.24 | 10| 9978.8 | 8111.6 | |
| 2-swap + Greedy | 100K | n_iters or when all 2-swap neighbors of graph have been visited | 0.11 | 10 | 6723.4 | 6664.1 | |
| 3-swap | 100K | n_iters or when all 3-swap neighbors of graph have been visited | 6.75 | 10 | 9349.3 | 7937.7 | |
| 3-swap + Greedy | 100K | n_iters or when all 3-swap neighbors of graph have been visited | 4.12 | 10 | 6659.4 | 6659.4 | |
| 2-opt | 10K | n_iters or when all 2-opt neighbors of graph have been visited | 0.1 | 10 | 7353.0 | 6659.4 | |
| 2-opt + Greedy | 10K | n_iters or when all 2-opt neighbors of graph have been visited | 0.01 | 10 | 6694.6 | 6664.1 | |

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
| Greedy | 250K | when Hamiltonian | 0.36 | 10 | 12346.9 | 12346.9 | |
| 2-swap | 250K | n_iters or when all 2-swap neighbors of graph have been visited | 39.7 | 10| 20028.8 | 18409.6 | |
| 2-swap + Greedy | 250K | n_iters or when all 2-swap neighbors of graph have been visited | 8.1 | 10 | 11515.8 | 11318.5 | |
| 2-opt | 250K | n_iters or when all 2-opt neighbors of graph have been visited | 32.2 | 10 | 10520.8 | 10108.0 | |
| 2-opt + Greedy | 250K | n_iters or when all 2-opt neighbors of graph have been visited | 11.9 | 10 | 10078.4 | 9931.1 | |

<p align="center">
  <img src="tsp/gif/qa194_2_opt_greedy.gif" width="24%">
</p>
<p align="center">
  2-opt with greedy initialization applied to qa194
</p>
