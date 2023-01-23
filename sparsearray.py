#hacker rank problem splarse array
def matchingStrings(stringList, queries):
    c = {}
    rslt = []
    for i in stringList:
        if i not in c:
            c[i] = 1
        else:
            c[i] += 1

    for i in queries:
        if i in c:
            rslt.append(c[i])
        else:
            rslt.append(0)

    return rslt
