#from hacker rank problem equalize the array
def equalizeArray(arr):
    c = 0
    dic = {}
    for i in arr:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    k = len(arr) - max(dic.values())

    return k

#we rest the total number of things in the array - the number of times the
#value that is repeated the most
