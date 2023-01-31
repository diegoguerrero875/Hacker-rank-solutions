#from hacker rank angry professor problem
def angryProfessor(k, a):
    c = 0
    for i in a:
        if i <= 0:
            c += 1

    if c < k:
        return "YES"
    else:
        return "NO"
