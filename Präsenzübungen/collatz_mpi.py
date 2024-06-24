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

if __name__ == "__main__":
    main()
