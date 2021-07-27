def solution(strings, n):
    stringDict = {}
    for string in strings:
        if not string[n] in stringDict:
            stringDict[string[n]] = []
        stringDict[string[n]].append(string)
        
    result = []
    for stringList in list(map(lambda char: stringDict[char] ,sorted(stringDict.keys()))):
        result += sorted(stringList)
    return result