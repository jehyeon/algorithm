import numpy as np
    
def solution(n, arr1, arr2):
    toBin = lambda number: list(map(int, list('0' * (n - len(bin(number)[2:])) + bin(number)[2:])))
    lines = (np.array(list(map(toBin, arr1))) + np.array(list(map(toBin, arr2)))).tolist()
    return [ ''.join(['#' if block > 0 else ' ' for block in line]) for line in lines]