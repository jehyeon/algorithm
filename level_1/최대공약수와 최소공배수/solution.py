def solution(n, m):
    if m > n: n, m = m, n
    gcd = getGcd(n, m)
    return gcd, getLcm(n, m, gcd)

def getGcd(b, s):
    # big, small
    if b % s == 0:
        return s

    b, s = s, b % s
    
    return getGcd(b, s)

def getLcm(n, m, gcd):
    return int(n / gcd * m / gcd * gcd)