import math
import numpy as np
import multiprocessing as mp


ymin = -100.0
ymax = 100.0
xmin = -100.0
xmax = 100.0
nx = 101 
ny = 101
dx = (xmax - xmin) / (nx - 1)
dy = (ymax - ymin) / (ny - 1)

y_grid = np.linspace(ymin, ymax, ny)


def f(y):
    x_grid = np.linspace(xmin, xmax, nx)
    sum_result = 0
    for x in x_grid:
        sum_result += math.exp(-(x*x + y*y + y)) * dx
    return sum_result * dy


if __name__ == '__main__':
    pool = mp.Pool()
    result = pool.map(f, y_grid)
    pool.close()
    pool.join()
    total_sum = sum(result)
    
   
    print(total_sum)
