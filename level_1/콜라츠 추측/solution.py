def solution(num):
    count = 0
    if num == 1:
        return count
    
    while True:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
        count += 1
        
        if num == 1:
            return count
        
        if count > 499:
            return -1