def ggt(p, q):
    """ Berechnet den größten gemeinsamen Teiler ggt(p,q) der ganzen Zahlen
        p > 0 und q > 0."""
    
    if type(p) != int or type(q) != int:
        raise TypeError("Alle Inputs müssen ganze Zahlen sein.")
    
    if p < 0 or q < 0:
        raise ValueError("Alle Inputs müssen positiv sein.")
    
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

#print(ggt(True, 3))