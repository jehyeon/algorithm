def solution(arr, divisor):
    answer = sorted(filter(lambda item: item % divisor == 0, arr))
    return [-1] if len(answer) == 0 else answer