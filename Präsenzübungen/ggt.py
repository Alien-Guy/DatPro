def ggt(p, q):
    """ Berechnet den größten gemeinsamen Teiler ggt(p,q) der ganzen Zahlen
        p > 0 und q > 0."""

    while True:
        r = p % q
        if r == 0:
            break
        p = q
        q = r

    return q


def main():
    print(f"ggt(3*7, 3*19) = {ggt(3*7, 3*19)}")

if __name__ == "__main__":
    main()
