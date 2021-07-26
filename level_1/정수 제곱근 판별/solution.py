def solution(n):
    return (n ** (1/2) + 1) ** 2 if n ** (1/2) % 1 == 0.0 or n ** (1/2) % 1 >= 1 else  -1