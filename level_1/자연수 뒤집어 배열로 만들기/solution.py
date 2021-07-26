def solution(n):
    result = list(str(n))
    result.reverse()
    return list(map(int, result))