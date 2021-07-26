def solution(s):
    result = []
    for word in s.split(' '):
        result.append(''.join([item.upper() if index % 2 == 0 else item.lower() for index, item in enumerate(word)]))
        
    return ' '.join(result)