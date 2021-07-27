def solution(n):
    result = list(range(n + 1))
    for index in result[2:]:
        a = 2
        while not result[index] == False and index * a < n + 1:
            result[index * a] = False
            a += 1
    
    return len(list(filter(lambda item: item != False, result[2:])))
