def solution(numbers):
    answer = []
    numbers.sort()
    for i in range(len(numbers) + 1):
        for j in range(i + 1, len(numbers) + 1):
            try:
                answer.append(numbers[i] + numbers[j])
            except:
                break
        
    return sorted(list(set(answer)))