def solution(s):
    return list(s).count('p') + list(s).count('P') == list(s).count('y') + list(s).count('Y')