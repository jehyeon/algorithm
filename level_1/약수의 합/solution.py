def solution(n):
    return sum([div if n % div == 0 else 0 for div in range(1, n + 1)])