def solution(arr1, arr2):
    return [[col + arr2[i][j] for j, col in enumerate(rows)] for i, rows in enumerate(arr1)]