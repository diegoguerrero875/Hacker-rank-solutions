#the hurdle race problem on hacker rank
def hurdleRace(k, height):
    c = 0
    lista = []
    for i in height:
        if i > k:
            c = i - k
            lista.append(c)

    if c == 0:
        return c
    else:
        return max(lista)
