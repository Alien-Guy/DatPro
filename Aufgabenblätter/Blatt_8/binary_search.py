def binary_search(data, element, lower, upper):
# diese Routine rekursiv implementieren...
    pass


def search_sorted(data, element):
    if all(data[i] <= data[i+1] for i in range(len(data) - 1)):
        return binary_search(data, element, 0, len(data) - 1)
    else:
        raise ValueError


l = [0, 1, 2, 3, 4, 4, 6, 7, 8, 9, 10, 12, 12, 13, 14, 15, 16, 17, 18, 19]
print(f"11: {search_sorted(l, 11)}") # False
print(f"12: {search_sorted(l, 12)}") # True

