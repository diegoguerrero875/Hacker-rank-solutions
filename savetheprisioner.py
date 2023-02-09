#from hacker rank problem save the prisioner
#this solution gets the answer but very slow
def saveThePrisoner(n, m, s):
    c = 1
    dic = {}
    for i in range(1, n  + 1):
        if i not in dic:
            dic[i] = 0
            
        
    while c < m:
        dic[s] += 1
        c += 1
        if s == n:
            s = 1
        else:
            s += 1
        
            
    return s

#even tho it satisfy the needs it does terrubly in some scenarios here a better
#version
def saveThePrisoner(n, m, s):
    return (s + m - 1) % n or n

#And thats why computers will take all our jobs, the last one is from ChatGTP
