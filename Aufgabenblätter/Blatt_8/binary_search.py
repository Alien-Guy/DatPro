#Aufgabenblatt 7
#Autor: Jonas Niermann; Matr.-Nr.: 7418131

# Programm definiert die Routine binary_search, die in einer geordneten Liste von Zahlen
# rekursiv nach einer vorgegebnen Zahl sucht.

def binary_search(data, element, lower, upper):
    mid = lower + (upper-lower)//2
    if lower == upper:      # in this case is lower == upper == mid
        if data[mid] == element:
            return True
        else:
            return False
    
    else:
        if data[mid] == element:
            return True
        elif data[mid] > element:
            return binary_search(data, element, lower, mid-1)
        elif data[mid] < element:
            return binary_search(data, element, mid+1, upper)
    pass


def search_sorted(data, element):
    if all(data[i] <= data[i+1] for i in range(len(data) - 1)):
        return binary_search(data, element, 0, len(data) - 1)
    else:
        raise ValueError


l = [0, 1, 2, 3, 4, 4, 6, 7, 8, 9, 10, 12, 12, 13, 14, 15, 16, 17, 18, 19]
print(f"11: {search_sorted(l, 11)}") # False
print(f"12: {search_sorted(l, 12)}") # True