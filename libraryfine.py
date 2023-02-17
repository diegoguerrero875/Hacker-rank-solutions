#from hacker rank problem Library Fine
def libraryFine(d1, m1, y1, d2, m2, y2):

    k = 0
    if y1 > y2:
        k += 10000
    elif m1 > m2 and y1 - y2 == 0:
        k += (m1 - m2)*500
    elif d1 > d2 and m2 - m1 == 0 and y1 - y2 == 0:
        k += (d1 - d2)*15

    return k
