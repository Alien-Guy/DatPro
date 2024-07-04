import multiprocessing as mp
import math
import numpy as np

ymin = -100.0
ymax =  100.0
xmin = -100.0
xmax =  100.0
nx = 1001
ny = 1001
dx = (xmax - xmin)/(nx - 1)
dy = (ymax - ymin)/(ny - 1)
N_PROC = 5

def f(x, y):
    return math.exp(-(x*x + y*y + y))


def worker(q_work , q_result):
    print("work")
    sumx = 0.
    x_grid = np.linspace(xmin, xmax, nx)
    while True:
        y = q_work.get()
        print("y", y)
        if y == None:
            return
        for x in x_grid:
            sumx += f(x,y)*dx
        q_result.put(sumx)

def consumer(q_result):
    print("cons")
    result = 0.
    n = 0
    while n < ny-1:
        print("n", n)
        if n==5:
            break
        g = q_result.get()
        result += g*dy
        n+=1
    print(f"das Integral ist { result}")
    return

def main():
    print("A")
    q_work = mp.Queue()
    q_result = mp.Queue()
    y_grid = np.linspace(ymin, ymax, ny)
    
    print("B")  
    process = []
    process.append(mp.Process(target=consumer, args=(q_result, )))
    process[0].start()
    
    for n in range(1,N_PROC):
        process.append(mp.Process(target=worker, args=(q_work, q_result)))
        process[n].start()
    print("C")     
    for y in y_grid:
        q_work.put(y)
    for n in range(N_PROC):
        q_work.put(None)
   
    print("D")       
    for n in range(N_PROC):
            process[n].join()



if __name__ == '__main__':
    main()