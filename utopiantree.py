#from hacker rank utopian tree problem
def utopianTree(n):
    tot = 1
    for i in range(1, n + 1):
        if i % 2 == 0:
            tot += 1
        else:
            tot *= 2
    return tot
