#from hacker rank problem viral advertising
def viralAdvertising(n):
    s = 6
    l = 2
    t = 2
    mf = 3
    if n == 1:
        return t
    else:
        for i in range(2, n + 1):
            l = s // 2
            t += l
            s = l * mf
        return t
