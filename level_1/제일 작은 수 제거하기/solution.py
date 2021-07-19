def solution(arr):
    del arr[arr.index(min(arr))]
    return arr if len(arr) > 0 else [-1]