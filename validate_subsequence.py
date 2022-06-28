
def isValidSubsequence(array, sequence):
    # Write your code here.
    subsq = True
    pointer = 0
    
    for i in array:
        if sequence[pointer] == i:
            subsq = True
            pointer = pointer + 1
            if pointer == len(sequence):
                return subsq
        else:
            subsq = False

    if pointer != len(sequence):
        subsq = False
    
    return subsq
