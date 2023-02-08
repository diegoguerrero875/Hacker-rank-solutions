#from hacker rank problem Sequence Equation
def permutationEquation(p):
    c = 1
    lar = len(p)
    dic = {}
    tot = []
    vari = 0
    for i in p:
        if i not in dic:
            dic[i] = c
        c += 1

    for i in range(1, lar + 1):
        vari = dic[i]
        tot.append(dic[vari])
