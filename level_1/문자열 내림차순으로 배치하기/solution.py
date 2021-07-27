def solution(s):
    return ''.join(sorted(list(s), reverse=True, key=lambda item: ord(item)))