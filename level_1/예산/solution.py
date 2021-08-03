def solution(d, budget):
    sortedD = sorted(d)
    while sum(sortedD) > budget:
        sortedD.pop()
    return len(sortedD)