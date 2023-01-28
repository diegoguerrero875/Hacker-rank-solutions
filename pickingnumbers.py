#from hacker rank picking numbers problem
def pickingNumbers(a):
    c = [0] * (max(a) + 1)
    for num in a:
        c[num] += 1
    l = 0
    for i in range(len(c) - 1):
        l = max(l, c[i] + c[i + 1])
    return l
