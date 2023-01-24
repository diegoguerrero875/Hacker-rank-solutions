#find digits problem on hakcer rank
def findDigits(n):
    conv = str(n)
    c = 0
    for i in conv:
        if int(i) != 0 and n % int(i) == 0:
            c += 1
    return c
