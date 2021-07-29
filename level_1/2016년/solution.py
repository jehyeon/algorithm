def solution(a, b):
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    return ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED'][(sum(month[:a]) + b) % 7]