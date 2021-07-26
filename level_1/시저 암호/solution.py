def solution(s, n):
    result = ''
    for item in list(s):
        if item == ' ':
            result += item
        
        if item.isupper():
            if ord(item) + n > 90:
                result += chr(ord(item) + n - 26)
            else:
                result += chr(ord(item) + n)
                
        if item.islower():
            if ord(item) + n > 122:
                result += chr(ord(item) + n - 26)
            else:
                result += chr(ord(item) + n)
                
    return result