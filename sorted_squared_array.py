def sortedSquaredArray(array):
    # Write your code here.

    squared = list(map(lambda x: x**2, array))
    return sorted(squared)
