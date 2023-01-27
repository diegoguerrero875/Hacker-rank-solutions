#from hacker rank electronic shop problem
def getMoneySpent(keyboards, drives, b):
    maxv = []
    for i in keyboards:
        for j in drives:
            if i + j <= b:
                maxv.append(i+j)

    if min(keyboards) + min(drives) > b:
        return -1
    else:
        return max(maxv)
