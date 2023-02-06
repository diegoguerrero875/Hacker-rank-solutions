#from hacker rank problem beautiful days at the movies
def beautifulDays(i, j, k):
    c = 0
    for e in range(i, j+1):
        r = str(e)
        re = r[::-1]
        if (e - int(re)) % k == 0:
            c += 1
