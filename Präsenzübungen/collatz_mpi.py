from mpi4py import MPI

def worker(comm):
    s = MPI.Status()
    while True:
        n = comm.recv(source = 0, status = s)
        länge = 0
        if s.Get_tag() == ENDTAG:
            return
        länge = collatz_länge(n)
        T = (länge, n)
        comm.send(T, dest = 0)




def collatz_länge(n):
    länge = 0
    while n != 1:
        if n%2 == 0:
            n //= 2
        else:
            n = 3*n + 1
        länge += 1
    return länge


def main():
    N = 100000000
    l_max = 0
    m_max = 0
    for m in range(1, N + 1):
        l = collatz_länge(m)
        if l > l_max:
            l_max = l
            m_max = m
            print(f"neues Maximum collatz_länge({m_max}) = {l_max}")
    print(f"Maximum:collatz_länge({m_max}) = {l_max}")

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    if rank == 0:
        dispatcher(comm)
    else:
        worker(comm)

#if __name__ == "__main__":
#    main()
